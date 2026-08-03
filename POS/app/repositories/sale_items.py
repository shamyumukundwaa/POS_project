from app.models.sale_items import SaleItem
from app.repositories.base import BaseRepository


class SaleItemRepository(BaseRepository[SaleItem]):
    def __init__(self):
        super().__init__(SaleItem)


sale_item_repo = SaleItemRepository()
