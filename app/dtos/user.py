from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig
from app.models import User

class UserReadDTO(SQLAlchemyDTO[User]):
    # Profundidad 0: Solo muestra datos del usuario, no sus préstamos
    config = SQLAlchemyDTOConfig(
        max_nested_depth=0,
        exclude={"password", "loans", "reviews"}
    )

class UserCreateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(
        exclude={"id", "created_at", "updated_at", "loans", "reviews", "is_active"},
    )

class UserUpdateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(
        exclude={"id", "created_at", "updated_at", "loans", "reviews", "is_active", "password"},
        partial=False # <--- FIX
    )

class UserLoginDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(include={"username", "password"})