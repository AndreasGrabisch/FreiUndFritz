"""Client for the Anny booking / access management API."""

from datetime import datetime
from typing import Optional
import logging

import requests

from freiundfritz.models.booking import Booking

logger = logging.getLogger(__name__)


class AnnyClient:
    """Thin wrapper around the Anny REST API.

    See https://www.anny.co for API documentation.
    """

    def __init__(self, base_url: str, api_key: str, timeout: int = 10) -> None:
        self.base_url = base_url.rstrip("/")
        self._session = requests.Session()
        self._session.headers.update(
            {
                "Authorization": f"******",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )
        self.timeout = timeout

    # ------------------------------------------------------------------
    # Booking queries
    # ------------------------------------------------------------------

    def get_active_booking(
        self, resource_id: str, user_id: str, at: Optional[datetime] = None
    ) -> Optional[Booking]:
        """Return the active Anny booking for *resource_id* / *user_id* at *at*.

        Returns ``None`` when no matching booking is found.
        """
        at = at or datetime.utcnow()
        params = {
            "resource_id": resource_id,
            "user_id": user_id,
            "at": at.isoformat(),
        }
        try:
            response = self._session.get(
                f"{self.base_url}/bookings/active",
                params=params,
                timeout=self.timeout,
            )
            response.raise_for_status()
        except requests.RequestException as exc:
            logger.error("Anny API error: %s", exc)
            raise

        data = response.json()
        if not data:
            return None

        return Booking(
            id=data["id"],
            room_id=resource_id,
            user_id=user_id,
            start=datetime.fromisoformat(data["start"]),
            end=datetime.fromisoformat(data["end"]),
            anny_booking_id=data["id"],
        )

    def has_access(self, resource_id: str, user_id: str) -> bool:
        """Return ``True`` when the user currently has an active booking."""
        try:
            return self.get_active_booking(resource_id, user_id) is not None
        except requests.RequestException:
            return False
