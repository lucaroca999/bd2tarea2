from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig
from app.models import Book

class BookReadDTO(SQLAlchemyDTO[Book]):
    # Profundidad 0 para evitar ciclos con Categorias o Préstamos
    config = SQLAlchemyDTOConfig(max_nested_depth=0)

class BookCreateDTO(SQLAlchemyDTO[Book]):
    config = SQLAlchemyDTOConfig(
        exclude={"id", "created_at", "updated_at", "loans", "reviews", "categories"},
    )

class BookUpdateDTO(SQLAlchemyDTO[Book]):
    # Desactivamos partial para que Swagger no explote 
    config = SQLAlchemyDTOConfig(
        exclude={"id", "created_at", "updated_at", "loans", "reviews", "categories"},
        partial=False 
    )