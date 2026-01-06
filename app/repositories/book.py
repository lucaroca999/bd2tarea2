from typing import Sequence
from advanced_alchemy.repository import SQLAlchemySyncRepository
from sqlalchemy import select, func, desc

from app.models import Book, Review, Category

class BookRepository(SQLAlchemySyncRepository[Book]):
    """Repository for Book operations."""
    model_type = Book

    def get_available_books(self) -> Sequence[Book]:
        """Retornar libros con stock > 0."""
        return self.list(Book.stock > 0)

    def find_by_category(self, category_id: int) -> Sequence[Book]:
        """Buscar libros de una categoría."""
        statement = select(Book).join(Book.categories).where(Category.id == category_id)
        return self.session.scalars(statement).all()

    def get_most_reviewed_books(self, limit: int = 10) -> Sequence[Book]:
        """Libros ordenados por cantidad de reseñas."""
        statement = (
            select(Book)
            .outerjoin(Book.reviews)
            .group_by(Book.id)
            .order_by(desc(func.count(Review.id)))
            .limit(limit)
        )
        return self.session.scalars(statement).all()

    def update_stock(self, book_id: int, quantity: int) -> Book:
        """Actualizar stock de un libro y GUARDAR CAMBIOS."""
        book = self.get(book_id)
        
        new_stock = book.stock + quantity
        if new_stock < 0:
            raise ValueError("Stock cannot be negative")
            
        book.stock = new_stock
        self.session.add(book)
        
        # commit() guarda el cambio permanentemente
        self.session.commit()
        # refresh() actualiza el objeto con los datos de la BD
        self.session.refresh(book)
        
        return book

    def search_by_author(self, author_name: str) -> Sequence[Book]:
        """Buscar libros por nombre de autor (parcial)."""
        return self.list(Book.author.ilike(f"%{author_name}%"))