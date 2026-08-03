from app.models.sales import Sale
from app.repositories.base import BaseRepository


class SaleRepository(BaseRepository[Sale]):
    def __init__(self):
        super().__init__(Sale)


sale_repo = SaleRepository()
