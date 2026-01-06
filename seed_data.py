"""
Script para poblar la base de datos con datos de prueba.
"""
import random
from datetime import date, timedelta
from decimal import Decimal

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from pwdlib import PasswordHash

from app.config import settings
from app.models import User, Book, Category, Loan, Review, LoanStatus

engine = create_engine(settings.database_url)
password_hasher = PasswordHash.recommended()

def seed():
    print("Iniciando carga de datos...")
    
    with Session(engine) as session:
        # Limpieza inicial
        session.query(Review).delete()
        session.query(Loan).delete()
        session.query(User).delete()
        
        # Categorías
        cat_names = ["Ficción", "No Ficción", "Ciencia", "Historia", "Fantasía"]
        categories = []
        for name in cat_names:
            cat = Category(name=name, description=f"Libros de tipo {name}")
            categories.append(cat)
            session.add(cat)
        session.flush()

        # Libros
        books = []
        base_isbn_num = 1120
        
        for i in range(10):
            seq_num = base_isbn_num + (i * 5)
            isbn = f"ISBN-BD2-2025-{seq_num}"
            
            book = Book(
                title=f"Libro {i+1}",
                author=f"Autor {i+1}",
                isbn=isbn,
                pages=random.randint(100, 500),
                published_year=random.randint(1950, 2024),
                stock=5,
                language="es",
                publisher="Editorial UMAG",
                description="Descripción genérica del libro."
            )
            book.categories = random.sample(categories, k=random.randint(1, 2))
            books.append(book)
            session.add(book)
        
        session.flush()

        # Usuarios
        users = []
        hashed_pw = password_hasher.hash("password123")
        
        for i in range(5):
            user = User(
                username=f"user{i+1}",
                fullname=f"Usuario Prueba {i+1}",
                password=hashed_pw,
                email=f"user{i+1}@example.com",
                phone=f"+5691234567{i}",
                address=f"Calle {123+i}",
                is_active=True
            )
            users.append(user)
            session.add(user)
            
        session.flush()

        # Préstamos
        today = date.today()
        
        # Activos
        for i in range(3):
            loan = Loan(
                user=users[i],
                book=books[i],
                loan_dt=today - timedelta(days=2),
                due_date=today + timedelta(days=12),
                status=LoanStatus.ACTIVE,
                return_dt=None
            )
            session.add(loan)

        # Devueltos
        for i in range(3):
            loan = Loan(
                user=users[i],
                book=books[i+3],
                loan_dt=today - timedelta(days=20),
                due_date=today - timedelta(days=6),
                status=LoanStatus.RETURNED,
                return_dt=today - timedelta(days=10),
                fine_amount=Decimal(0)
            )
            session.add(loan)

        # Vencidos
        for i in range(2):
            loan = Loan(
                user=users[4],
                book=books[i+6],
                loan_dt=today - timedelta(days=30),
                due_date=today - timedelta(days=16),
                status=LoanStatus.OVERDUE,
                return_dt=None
            )
            session.add(loan)

        # Reseñas
        for i in range(15):
            user = random.choice(users)
            book = random.choice(books)
            
            exists = session.scalar(
                select(Review).where(Review.user_id == user.id, Review.book_id == book.id)
            )
            if not exists:
                review = Review(
                    rating=random.randint(1, 5),
                    comment="Muy bueno." if random.random() > 0.5 else "Regular.",
                    review_date=today - timedelta(days=random.randint(0, 60)),
                    user=user,
                    book=book
                )
                session.add(review)
        
        session.commit()
        print("Datos cargados correctamente.")

if __name__ == "__main__":
    seed()