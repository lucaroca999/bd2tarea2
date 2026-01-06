from advanced_alchemy.repository import SQLAlchemySyncRepository
from app.models import Category

class CategoryRepository(SQLAlchemySyncRepository[Category]):
    """Repository for Category operations."""
    model_type = Category