from app.models.payments import Payment
from app.repositories.base import BaseRepository


class PaymentRepository(BaseRepository[Payment]):
    def __init__(self):
        super().__init__(Payment)


payment_repo = PaymentRepository()
