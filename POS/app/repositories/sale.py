from sqlalchemy.orm import Session
from typing import Optional, List
from app.models.sales import Sale


class SaleRepository:
    def get_by_id(self, db: Session, sale_id: int) -> Optional[Sale]:
        return db.query(Sale).filter(Sale.sale_id == sale_id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[Sale]:
        return db.query(Sale).offset(skip).limit(limit).all()

    def create(self, db: Session, sale_obj: Sale) -> Sale:
        db.add(sale_obj)
        db.commit()
        db.refresh(sale_obj)
        return sale_obj


sale_repo = SaleRepository()
