"""Book controller."""
from litestar import Controller, get, post, patch, delete
from litestar.di import Provide
from litestar.exceptions import ValidationException
from sqlalchemy.orm import Session # <--- Importante

from app.models import Book
from app.repositories.book import BookRepository

# --- FUNCIÓN PUENTE (SOLUCIÓN AL ERROR 400) ---
def provide_book_repo(db_session: Session) -> BookRepository:
    """
    Esta función toma la 'db_session' que ofrece el plugin
    y crea el repositorio manualmente.
    """
    return BookRepository(session=db_session)
# ---------------------------------------------

class BookController(Controller):
    path = "/books"
    tags = ["Books"]
    
    # FIX: Usar la función puente en lugar de la clase directa
    dependencies = {"repository": Provide(provide_book_repo)}

    @get()
    def list_books(self, repository: BookRepository) -> list[Book]:
        return repository.list()
    
    @get("/available")
    def get_available(self, repository: BookRepository) -> list[Book]:
        return repository.get_available_books()

    @get("/{book_id:int}")
    def get_book(self, book_id: int, repository: BookRepository) -> Book:
        return repository.get(book_id)

    @post()
    def create_book(self, data: dict, repository: BookRepository) -> Book:
        # Validación manual simple
        if "stock" in data and data["stock"] <= 0:
             raise ValidationException("Stock must be > 0")
        
        # Convertimos dict a Modelo
        obj = Book(**data)
        return repository.add(obj)

    @patch("/{book_id:int}")
    def update_book(self, book_id: int, data: dict, repository: BookRepository) -> Book:
        if "stock" in data and data["stock"] < 0:
             raise ValidationException("Stock cannot be negative")
             
        # Actualización manual
        book = repository.get(book_id)
        for key, value in data.items():
            if hasattr(book, key):
                setattr(book, key, value)
                
        return repository.update(book)

    @delete("/{book_id:int}")
    def delete_book(self, book_id: int, repository: BookRepository) -> None:
        repository.delete(book_id)