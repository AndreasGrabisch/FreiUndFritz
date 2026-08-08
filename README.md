# FreiUndFritz – Bewohnerapp

Door and room access management for residents, powered by **Anny** bookings and electric door locks.

## Overview

FreiUndFritz lets residents and guests unlock rooms that they have booked through [Anny](https://www.anny.co).  When a resident requests access, the system:

1. Checks Anny for an active booking that covers the current time.
2. Issues a short-lived `AccessToken` if a valid booking exists.
3. Sends an unlock command to the electric door lock via a REST-capable lock controller (e.g. Nuki Web API).

## Project Structure

```
freiundfritz/
  models/           – Domain models (Room, User, Booking, AccessToken)
  integrations/     – Anny API client & door lock controller
  services/         – AccessService: orchestrates booking checks + lock control
  tests/            – Unit tests
pyproject.toml      – Project metadata & dependencies
```

## Getting Started

```bash
pip install -e ".[dev]"
pytest
```

## Configuration

| Variable | Description |
|---|---|
| `ANNY_BASE_URL` | Base URL of the Anny REST API |
| `ANNY_API_KEY` | Anny API key |
| `LOCK_BASE_URL` | Base URL of the door lock REST gateway |
| `LOCK_API_KEY` | Lock gateway API key |

## Architecture

```
User request
    │
    ▼
AccessService.request_access(user, room)
    │
    ├─► AnnyClient.get_active_booking()  ──► Anny API
    │       valid booking found?
    │
    ├─► issues AccessToken
    │
    ▼
AccessService.unlock_with_token(token)
    │
    └─► DoorLockController.unlock(lock_id)  ──► Electric door lock
```
