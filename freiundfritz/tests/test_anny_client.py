"""Tests for AnnyClient."""

from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest
import requests

from freiundfritz.integrations.anny_client import AnnyClient


@pytest.fixture()
def client() -> AnnyClient:
    return AnnyClient(base_url="https://api.anny.example", api_key="test-key")


class TestHasAccess:
    def test_returns_true_when_booking_found(self, client):
        booking_data = {
            "id": "bk-1",
            "start": datetime.utcnow().isoformat(),
            "end": (datetime.utcnow()).isoformat(),
        }
        mock_resp = MagicMock()
        mock_resp.json.return_value = booking_data
        mock_resp.raise_for_status = MagicMock()

        with patch.object(client._session, "get", return_value=mock_resp):
            assert client.has_access("res-1", "user-1") is True

    def test_returns_false_when_no_booking(self, client):
        mock_resp = MagicMock()
        mock_resp.json.return_value = None
        mock_resp.raise_for_status = MagicMock()

        with patch.object(client._session, "get", return_value=mock_resp):
            assert client.has_access("res-1", "user-1") is False

    def test_returns_false_on_network_error(self, client):
        with patch.object(
            client._session, "get", side_effect=requests.ConnectionError("down")
        ):
            assert client.has_access("res-1", "user-1") is False
