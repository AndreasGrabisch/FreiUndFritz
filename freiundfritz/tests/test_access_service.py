"""Tests for the AccessService."""

from datetime import datetime, timedelta
from unittest.mock import MagicMock

import pytest

from freiundfritz.models.booking import Booking
from freiundfritz.models.room import Room
from freiundfritz.models.user import User
from freiundfritz.services.access_service import AccessService


def _make_booking(room_id: str, user_id: str, offset_minutes: int = 0) -> Booking:
    now = datetime.utcnow()
    return Booking(
        id="booking-1",
        room_id=room_id,
        user_id=user_id,
        start=now - timedelta(minutes=30) + timedelta(minutes=offset_minutes),
        end=now + timedelta(hours=1),
        anny_booking_id="anny-bk-1",
    )


@pytest.fixture()
def room() -> Room:
    return Room(
        id="room-1",
        name="Meetingraum A",
        lock_id="lock-001",
        anny_resource_id="anny-res-1",
    )


@pytest.fixture()
def user() -> User:
    return User(id="user-1", name="Alice", email="alice@example.com", anny_user_id="anny-u-1")


@pytest.fixture()
def service(room: Room, user: User):
    anny_client = MagicMock()
    lock_controller = MagicMock()
    lock_controller.unlock.return_value = True
    lock_controller.lock.return_value = True
    svc = AccessService(anny_client=anny_client, lock_controller=lock_controller)
    return svc, anny_client, lock_controller


class TestRequestAccess:
    def test_issues_token_when_booking_exists(self, service, room, user):
        svc, anny, _ = service
        anny.get_active_booking.return_value = _make_booking(room.id, user.id)

        token = svc.request_access(user, room)

        assert token is not None
        assert token.room_id == room.id
        assert token.user_id == user.id

    def test_returns_none_when_no_booking(self, service, room, user):
        svc, anny, _ = service
        anny.get_active_booking.return_value = None

        token = svc.request_access(user, room)

        assert token is None

    def test_returns_none_when_room_lacks_anny_id(self, service, user):
        svc, anny, _ = service
        room_no_anny = Room(id="r", name="R", lock_id="l")

        token = svc.request_access(user, room_no_anny)

        assert token is None
        anny.get_active_booking.assert_not_called()

    def test_returns_none_when_user_lacks_anny_id(self, service, room):
        svc, anny, _ = service
        user_no_anny = User(id="u", name="Bob", email="bob@example.com")

        token = svc.request_access(user_no_anny, room)

        assert token is None
        anny.get_active_booking.assert_not_called()


class TestUnlockWithToken:
    def test_unlocks_with_valid_token(self, service, room, user):
        svc, anny, lock = service
        anny.get_active_booking.return_value = _make_booking(room.id, user.id)

        token = svc.request_access(user, room)
        result = svc.unlock_with_token(token.token)

        assert result is True
        lock.unlock.assert_called_once_with(room.lock_id)

    def test_rejects_unknown_token(self, service, room, user):
        svc, _, lock = service
        result = svc.unlock_with_token("not-a-real-token")

        assert result is False
        lock.unlock.assert_not_called()

    def test_rejects_already_used_token(self, service, room, user):
        svc, anny, lock = service
        anny.get_active_booking.return_value = _make_booking(room.id, user.id)

        token = svc.request_access(user, room)
        svc.unlock_with_token(token.token)
        result = svc.unlock_with_token(token.token)

        assert result is False
        assert lock.unlock.call_count == 1


class TestLockRoom:
    def test_lock_room(self, service, room):
        svc, _, lock = service
        result = svc.lock_room(room)

        assert result is True
        lock.lock.assert_called_once_with(room.lock_id)
