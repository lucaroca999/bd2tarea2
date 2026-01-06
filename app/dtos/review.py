"""Data Transfer Objects for Review endpoints."""

from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig

from app.models import Review


class ReviewReadDTO(SQLAlchemyDTO[Review]):
    """DTO for reading review data."""
    
    config = SQLAlchemyDTOConfig(max_nested_depth=1)


class ReviewCreateDTO(SQLAlchemyDTO[Review]):
    """DTO for creating reviews."""

    config = SQLAlchemyDTOConfig(
        exclude={"id", "created_at", "updated_at", "review_date", "user", "book"},
    )


class ReviewUpdateDTO(SQLAlchemyDTO[Review]):
    """DTO for updating reviews."""

    config = SQLAlchemyDTOConfig(
        exclude={"id", "created_at", "updated_at", "review_date", "user_id", "book_id", "user", "book"},
        partial=True,
    )