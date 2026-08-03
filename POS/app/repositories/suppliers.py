from app.models.suppliers import Supplier
from app.repositories.base import BaseRepository


class SupplierRepository(BaseRepository[Supplier]):
    def __init__(self):
        super().__init__(Supplier)


supplier_repo = SupplierRepository()
