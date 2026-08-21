"""
base.py — Import all SQLModel table classes here so that
SQLModel.metadata.create_all() can discover every table in one place.
"""

# Import all models so their tables are registered on SQLModel.metadata
from app.features.flights.models import Flight  # noqa: F401
from app.features.users.models import User      # noqa: F401  (create when ready)
