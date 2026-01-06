"""Loan controller - Raw Mode."""
from datetime import date, timedelta
from litestar import Controller, get, post, patch
from litestar.di import Provide
from litestar.exceptions import ValidationException
from sqlalchemy.orm import Session

from app.models import Loan, LoanStatus
from app.repositories.loan import LoanRepository
from app.repositories.book import BookRepository 

# --- FUNCIONES PUENTE ---
def provide_loan_repo(db_session: Session) -> LoanRepository:
    return LoanRepository(session=db_session)

def provide_book_repo(db_session: Session) -> BookRepository:
    return BookRepository(session=db_session)
# ------------------------

class LoanController(Controller):
    path = "/loans"
    tags = ["Loans"]
    
    dependencies = {
        "repository": Provide(provide_loan_repo),
        "book_repository": Provide(provide_book_repo)
    }

    @get()
    def list_loans(self, repository: LoanRepository) -> list[Loan]:
        return repository.list()

    @get("/active")
    def get_active_loans(self, repository: LoanRepository) -> list[Loan]:
        return repository.get_active_loans()
        
    @get("/overdue")
    def get_overdue_loans(self, repository: LoanRepository) -> list[Loan]:
        return repository.get_overdue_loans()

    @get("/user/{user_id:int}")
    def get_user_history(self, user_id: int, repository: LoanRepository) -> list[Loan]:
        return repository.get_user_loan_history(user_id)

    @post()
    def create_loan(
        self, 
        data: dict, 
        repository: LoanRepository,
        book_repository: BookRepository 
    ) -> Loan:
        # 1. Validar Stock
        book_id = data.get("book_id")
        book = book_repository.get(book_id)
        if not book or book.stock < 1:
            raise ValidationException("Book is out of stock")

        # 2. Preparar objeto Loan
        new_loan = Loan(**data)

        # 3. Calcular fechas
        if not new_loan.loan_dt:
            new_loan.loan_dt = date.today()
        
        new_loan.due_date = new_loan.loan_dt + timedelta(days=14)
        new_loan.status = LoanStatus.ACTIVE
        
        # 4. Restar Stock (BookRepository ya hace commit internamente ahora)
        book_repository.update_stock(book_id, -1)
        
        # 5. Guardar Préstamo
        repository.add(new_loan)
        
        # Guardar el préstamo permanentemente
        repository.session.commit()
        repository.session.refresh(new_loan)
        
        return new_loan

    @post("/{loan_id:int}/return")
    def return_book(self, loan_id: int, repository: LoanRepository) -> Loan:
        return repository.return_book(loan_id)