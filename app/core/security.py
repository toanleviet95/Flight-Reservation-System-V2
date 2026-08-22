"""
Security utilities: JWT encoding/decoding, password hashing, etc.
Fill in as authentication features are implemented.
"""

from datetime import datetime, timedelta
from typing import Any

# Example: install python-jose and passlib to use these
# from jose import jwt, JWTError
# from passlib.context import CryptContext

SECRET_KEY = "change-me-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(subject: Any, expires_delta: timedelta | None = None) -> str:
    """Create a JWT access token. Requires python-jose."""
    raise NotImplementedError("Install python-jose and implement JWT logic here.")


def verify_token(token: str) -> dict:
    """Verify and decode a JWT token."""
    raise NotImplementedError("Implement token verification here.")
