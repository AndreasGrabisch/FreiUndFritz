"""Core access-control service.

Ties together Anny booking checks and electric door lock control.
"""

from datetime import datetime
import logging
import secrets

from freiundfritz.integrations.anny_client import AnnyClient
from freiundfritz.integrations.door_lock_controller import DoorLockController
from freiundfritz.models.access_token import AccessToken
from freiundfritz.models.booking import Booking
from freiundfritz.models.room import Room
from freiundfritz.models.user import User

logger = logging.getLogger(__name__)


class AccessService:
    """Orchestrates door access by verifying Anny bookings and controlling locks."""

    def __init__(
        self,
        anny_client: AnnyClient,
        lock_controller: DoorLockController,
    ) -> None:
        self._anny = anny_client
        self._lock = lock_controller
        # In-memory token store; replace with a persistent store in production.
        self._tokens: dict[str, AccessToken] = {}
        self._token_lock_ids: dict[str, str] = {}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def request_access(self, user: User, room: Room) -> AccessToken | None:
        """Verify the user's Anny booking and issue an :class:`AccessToken`.

        Returns ``None`` when the user has no valid booking for the room.
        """
        if not room.anny_resource_id or not user.anny_user_id:
            logger.warning(
                "Room %s or user %s lacks Anny IDs – access denied.",
                room.id,
                user.id,
            )
            return None

        booking = self._anny.get_active_booking(
            resource_id=room.anny_resource_id,
            user_id=user.anny_user_id,
        )
        if booking is None:
            logger.info("No active booking for user %s in room %s.", user.id, room.id)
            return None

        token = self._create_token(user, room, booking)
        logger.info(
            "Access token issued for user %s / room %s (booking %s).",
            user.id,
            room.id,
            booking.id,
        )
        return token

    def unlock_with_token(self, token_value: str) -> bool:
        """Consume *token_value* and unlock the associated door.

        Returns ``True`` on success, ``False`` when the token is invalid,
        expired, or already used.
        """
        token = self._tokens.get(token_value)
        if token is None:
            logger.warning("Unknown access token presented.")
            return False

        now = datetime.utcnow()
        if token.used:
            logger.warning("Access token %s already used.", token_value)
            return False
        if now < token.valid_from or now > token.valid_until:
            logger.warning("Access token %s is outside its validity window.", token_value)
            return False

        token.used = True
        # Retrieve the room's lock id (caller must provide room context in
        # production; here we embed the lock_id directly in the token store).
        lock_id = self._token_lock_ids.get(token_value, "")
        success = self._lock.unlock(lock_id)
        if success:
            logger.info("Door %s unlocked via token %s.", lock_id, token_value)
        return success

    def lock_room(self, room: Room) -> bool:
        """Manually lock a room's door."""
        return self._lock.lock(room.lock_id)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _create_token(self, user: User, room: Room, booking: Booking) -> AccessToken:
        token_value = secrets.token_urlsafe(32)
        token = AccessToken(
            token=token_value,
            room_id=room.id,
            user_id=user.id,
            booking_id=booking.id,
            valid_from=booking.start,
            valid_until=booking.end,
        )
        self._tokens[token_value] = token
        self._token_lock_ids[token_value] = room.lock_id
        return token
