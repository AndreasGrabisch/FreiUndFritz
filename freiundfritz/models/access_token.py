from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class AccessToken:
    """A short-lived token that authorises one unlock attempt."""

    token: str
    room_id: str
    user_id: str
    booking_id: str
    valid_from: datetime
    valid_until: datetime
    used: bool = False
