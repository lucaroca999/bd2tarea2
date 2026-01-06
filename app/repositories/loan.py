from typing import Sequence
from datetime import date
from decimal import Decimal

from advanced_alchemy.repository import SQLAlchemySyncRepository
from sqlalchemy import select

from app.models import Loan, LoanStatus

class LoanRepository(SQLAlchemySyncRepository[Loan]):
    """Repository for Loan operations."""
    model_type = Loan

    def get_active_loans(self) -> Sequence[Loan]:
        return self.list(Loan.status == LoanStatus.ACTIVE)

    def get_overdue_loans(self) -> Sequence[Loan]:
        today = date.today()
        statement = select(Loan).where(
            Loan.due_date < today,
            Loan.status == LoanStatus.ACTIVE
        )
        overdue_loans = self.session.scalars(statement).all()

        if overdue_loans:
            for loan in overdue_loans:
                loan.status = LoanStatus.OVERDUE
                self.session.add(loan)
            self.session.commit() # Guarda los cambios de estado

        return overdue_loans

    def calculate_fine(self, loan_id: int) -> Decimal:
        loan = self.get(loan_id)
        if not loan:
            return Decimal(0)

        check_date = loan.return_dt if loan.return_dt else date.today()
        
        if check_date <= loan.due_date:
            return Decimal(0)

        overdue_days = (check_date - loan.due_date).days
        fine = overdue_days * 500
        
        if fine > 50000:
            fine = 50000
            
        return Decimal(fine)

    def return_book(self, loan_id: int) -> Loan:
        """Procesar devolución y GUARDAR CAMBIOS."""
        loan = self.get(loan_id)
        
        if loan.status == LoanStatus.RETURNED:
            return loan

        loan.return_dt = date.today()
        loan.status = LoanStatus.RETURNED
        loan.fine_amount = self.calculate_fine(loan_id)
        
        if loan.book:
            loan.book.stock += 1
            self.session.add(loan.book)

        self.session.add(loan)
        
        # Guardar permanentemente
        self.session.commit()
        self.session.refresh(loan)
        
        return loan

    def get_user_loan_history(self, user_id: int) -> Sequence[Loan]:
        statement = select(Loan).where(Loan.user_id == user_id).order_by(Loan.loan_dt.desc())
        return self.session.scalars(statement).all()