from litestar import Controller, get, post, patch, delete
from litestar.di import Provide
from litestar.dto import DTOData

from app.models import Category
from app.repositories.category import CategoryRepository
from app.dtos.category import CategoryReadDTO, CategoryCreateDTO, CategoryUpdateDTO

class CategoryController(Controller):
    path = "/categories"
    tags = ["Categories"]
    return_dto = CategoryReadDTO
    dependencies = {"repository": Provide(CategoryRepository)}

    @get()
    def list_categories(self, repository: CategoryRepository) -> list[Category]:
        """Listar todas las categorías."""
        return repository.list()

    @get("/{category_id:int}")
    def get_category(self, category_id: int, repository: CategoryRepository) -> Category:
        """Obtener una categoría por su ID."""
        return repository.get(category_id)

    @post(dto=CategoryCreateDTO)
    def create_category(self, data: Category, repository: CategoryRepository) -> Category:
        """Crear una nueva categoría."""
        return repository.add(data)

    @patch("/{category_id:int}", dto=CategoryUpdateDTO)
    def update_category(
        self, category_id: int, data: DTOData[Category], repository: CategoryRepository
    ) -> Category:
        """Actualizar una categoría existente."""
        category, _ = repository.get_and_update(id=category_id, **data.as_dict(exclude_unset=True))
        return category

    @delete("/{category_id:int}", return_dto=None)
    def delete_category(self, category_id: int, repository: CategoryRepository) -> None:
        """Eliminar una categoría."""
        repository.delete(category_id)