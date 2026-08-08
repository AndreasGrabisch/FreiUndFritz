from dataclasses import dataclass
from datetime import datetime


@dataclass
class Booking:
    """A confirmed Anny booking that grants a user access to a room."""

    id: str
    room_id: str
    user_id: str
    start: datetime
    end: datetime
    anny_booking_id: str
