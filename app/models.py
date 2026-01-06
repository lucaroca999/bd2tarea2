"""Database models for the library management system."""

from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from decimal import Decimal
from typing import Optional

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import ForeignKey, Table, Column, Integer, String, Date, Boolean, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship


class LoanStatus(str, Enum):
    ACTIVE = "ACTIVE"
    RETURNED = "RETURNED"
    OVERDUE = "OVERDUE"


# Tabla intermedia
book_categories = Table(
    "book_categories",
    BigIntAuditBase.metadata,
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
    Column("category_id", Integer, ForeignKey("categories.id"), primary_key=True),
)


class Category(BigIntAuditBase):
    """Category model."""
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[Optional[str]] = mapped_column(default=None)

    # ROMPEMOS EL CICLO AQUI:
    # books: Mapped[list["Book"]] = relationship(
    #     secondary=book_categories,
    #     back_populates="categories"
    # )


class User(BigIntAuditBase):
    """User model."""
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)
    fullname: Mapped[str]
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[Optional[str]] = mapped_column(default=None)
    address: Mapped[Optional[str]] = mapped_column(default=None)
    is_active: Mapped[bool] = mapped_column(default=True)

    # Mantenemos loans porque es vital, pero DTO lo controlará
    loans: Mapped[list["Loan"]] = relationship(back_populates="user")
    
    # ROMPEMOS EL CICLO AQUI:
    # reviews: Mapped[list["Review"]] = relationship(back_populates="user")


class Book(BigIntAuditBase):
    """Book model."""
    __tablename__ = "books"

    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    isbn: Mapped[str] = mapped_column(unique=True)
    pages: Mapped[int]
    published_year: Mapped[int]
    stock: Mapped[int] = mapped_column(default=1)
    description: Mapped[Optional[str]] = mapped_column(default=None)
    language: Mapped[str]
    publisher: Mapped[Optional[str]] = mapped_column(default=None)

    # Mantenemos loans
    loans: Mapped[list["Loan"]] = relationship(back_populates="book")
    
    # Mantenemos categories desde este lado para poder verlas al pedir un libro
    categories: Mapped[list["Category"]] = relationship(
        secondary=book_categories,
        # back_populates="books"  <-- Quitamos esto porque comentamos el otro lado
    )
    
    # ROMPEMOS EL CICLO AQUI:
    # reviews: Mapped[list["Review"]] = relationship(back_populates="book")


class Review(BigIntAuditBase):
    """Review model."""
    __tablename__ = "reviews"

    rating: Mapped[int]
    comment: Mapped[str]
    review_date: Mapped[date] = mapped_column(default=datetime.today)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))

    # Mantenemos la relación hacia arriba (Review -> User/Book) que es la importante
    user: Mapped[User] = relationship() # Quitamos back_populates
    book: Mapped[Book] = relationship() # Quitamos back_populates


class Loan(BigIntAuditBase):
    """Loan model."""
    __tablename__ = "loans"

    loan_dt: Mapped[date] = mapped_column(default=datetime.today)
    return_dt: Mapped[date | None]
    due_date: Mapped[date]
    fine_amount: Mapped[Optional[Decimal]] = mapped_column(Numeric(10, 2), default=None)
    status: Mapped[LoanStatus] = mapped_column(default=LoanStatus.ACTIVE)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))

    user: Mapped[User] = relationship(back_populates="loans")
    book: Mapped[Book] = relationship(back_populates="loans")


@dataclass
class PasswordUpdate:
    current_password: str
    new_password: str

@dataclass
class BookStats:
    total_books: int
    average_pages: float
    oldest_publication_year: int | None
    newest_publication_year: int | None