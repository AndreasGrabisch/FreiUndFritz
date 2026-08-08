from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Room:
    """A physical room or space protected by an electric door lock."""

    id: str
    name: str
    lock_id: str
    description: Optional[str] = None
    anny_resource_id: Optional[str] = None
