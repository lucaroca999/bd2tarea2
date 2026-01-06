"""User controller - Raw Mode."""
import re
from litestar import Controller, get, post, patch, delete
from litestar.di import Provide
from litestar.exceptions import ValidationException
from sqlalchemy.orm import Session

from app.models import User
from app.repositories.user import UserRepository

# --- FUNCIÓN PUENTE ---
def provide_user_repo(db_session: Session) -> UserRepository:
    return UserRepository(session=db_session)
# ----------------------

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

class UserController(Controller):
    path = "/users"
    tags = ["Users"]
    dependencies = {"repository": Provide(provide_user_repo)}

    @get()
    def list_users(self, repository: UserRepository) -> list[User]:
        return repository.list()

    @get("/{user_id:int}")
    def get_user(self, user_id: int, repository: UserRepository) -> User:
        return repository.get(user_id)

    @post()
    def create_user(self, data: dict, repository: UserRepository) -> User:
        # Validación manual
        if "email" in data and not re.match(EMAIL_REGEX, data["email"]):
            raise ValidationException(f"Invalid email format: {data['email']}")
        
        # Convertir a modelo
        user = User(**data)
        return repository.add(user)

    @patch("/{user_id:int}")
    def update_user(self, user_id: int, data: dict, repository: UserRepository) -> User:
        if "email" in data and not re.match(EMAIL_REGEX, data["email"]):
             raise ValidationException(f"Invalid email format")
             
        user = repository.get(user_id)
        for key, value in data.items():
            if hasattr(user, key):
                setattr(user, key, value)
        return repository.update(user)

    @delete("/{user_id:int}")
    def delete_user(self, user_id: int, repository: UserRepository) -> None:
        repository.delete(user_id)