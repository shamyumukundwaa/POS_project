from app.models.receipts import Receipt
from app.repositories.base import BaseRepository


class ReceiptRepository(BaseRepository[Receipt]):
    def __init__(self):
        super().__init__(Receipt)


receipt_repo = ReceiptRepository()
