from advanced_alchemy.repository import SQLAlchemySyncRepository
from app.models import Review

class ReviewRepository(SQLAlchemySyncRepository[Review]):
    """Repository for Review operations."""
    model_type = Review