"""Controller for electric door locks.

The controller abstracts the hardware interface so that the rest of the
application can remain hardware-agnostic.  A concrete implementation must
subclass :class:`DoorLockController` and implement :meth:`unlock` and
:meth:`lock`.
"""

from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)


class DoorLockController(ABC):
    """Abstract base class for electric door lock controllers."""

    @abstractmethod
    def unlock(self, lock_id: str) -> bool:
        """Send an *unlock* command to the door identified by *lock_id*.

        Returns ``True`` on success, ``False`` otherwise.
        """

    @abstractmethod
    def lock(self, lock_id: str) -> bool:
        """Send a *lock* command to the door identified by *lock_id*.

        Returns ``True`` on success, ``False`` otherwise.
        """

    def is_locked(self, lock_id: str) -> bool:  # noqa: D401
        """Return the current lock state (``True`` = locked).

        Override this method if the hardware supports state queries.
        By default the result is not deterministic; subclasses should
        implement hardware-specific state queries.
        """
        raise NotImplementedError


class HttpDoorLockController(DoorLockController):
    """Door lock controller that communicates over HTTP/REST.

    Compatible with lock systems that expose a simple REST interface (e.g.
    Nuki Web API or generic smart-lock gateways).
    """

    def __init__(self, base_url: str, api_key: str, timeout: int = 5) -> None:
        import requests

        self.base_url = base_url.rstrip("/")
        self._session = requests.Session()
        self._session.headers.update(
            {
                "Authorization": f"******",
                "Content-Type": "application/json",
            }
        )
        self.timeout = timeout

    def unlock(self, lock_id: str) -> bool:
        import requests

        try:
            response = self._session.post(
                f"{self.base_url}/locks/{lock_id}/unlock",
                timeout=self.timeout,
            )
            response.raise_for_status()
            logger.info("Lock %s unlocked successfully.", lock_id)
            return True
        except requests.RequestException as exc:
            logger.error("Failed to unlock %s: %s", lock_id, exc)
            return False

    def lock(self, lock_id: str) -> bool:
        import requests

        try:
            response = self._session.post(
                f"{self.base_url}/locks/{lock_id}/lock",
                timeout=self.timeout,
            )
            response.raise_for_status()
            logger.info("Lock %s locked successfully.", lock_id)
            return True
        except requests.RequestException as exc:
            logger.error("Failed to lock %s: %s", lock_id, exc)
            return False

    def is_locked(self, lock_id: str) -> bool:
        import requests

        response = self._session.get(
            f"{self.base_url}/locks/{lock_id}",
            timeout=self.timeout,
        )
        response.raise_for_status()
        return response.json().get("locked", True)
