from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    """A resident or guest who may request door access."""

    id: str
    name: str
    email: str
    anny_user_id: Optional[str] = None
