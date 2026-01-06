from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig
from app.models import Loan

class LoanReadDTO(SQLAlchemyDTO[Loan]):
    config = SQLAlchemyDTOConfig(max_nested_depth=1)

class LoanCreateDTO(SQLAlchemyDTO[Loan]):
    config = SQLAlchemyDTOConfig(
        exclude={"id", "created_at", "updated_at", "user", "book", "due_date", "fine_amount", "status", "return_dt"},
    )

class LoanUpdateDTO(SQLAlchemyDTO[Loan]):
    config = SQLAlchemyDTOConfig(
        # Incluimos solo status y desactivamos partial
        include={"status"},
        partial=False
    )