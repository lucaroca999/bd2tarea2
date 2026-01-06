from litestar import Controller, get, post, delete
from litestar.di import Provide
from litestar.exceptions import ValidationException, HTTPException
from litestar.status_codes import HTTP_400_BAD_REQUEST

from app.models import Review
from app.repositories.review import ReviewRepository
from app.dtos.review import ReviewReadDTO, ReviewCreateDTO

class ReviewController(Controller):
    path = "/reviews"
    tags = ["Reviews"]
    return_dto = ReviewReadDTO
    dependencies = {"repository": Provide(ReviewRepository)}

    @get()
    def list_reviews(self, repository: ReviewRepository) -> list[Review]:
        return repository.list()

    @post(dto=ReviewCreateDTO)
    def create_review(self, data: Review, repository: ReviewRepository) -> Review:
        # Validación 1: Rating entre 1 y 5
        if not (1 <= data.rating <= 5):
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST, 
                detail="Rating must be between 1 and 5"
            )

        # Validación 2: Máximo 3 reseñas por usuario para el mismo libro
        # Contamos cuántas reseñas tiene ya este usuario para este libro
        existing_count = repository.count(user_id=data.user_id, book_id=data.book_id)
        if existing_count >= 3:
             raise ValidationException("User cannot create more than 3 reviews for the same book")

        return repository.add(data)

    @delete("/{review_id:int}", return_dto=None)
    def delete_review(self, review_id: int, repository: ReviewRepository) -> None:
        repository.delete(review_id)