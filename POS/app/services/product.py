from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.products import product_repo
from app.repositories.category import category_repo


class ProductService:
    def get_all(self, db: Session):
        return product_repo.get_multi(db)

    def get_by_id(self, db: Session, id_val: int):
        return product_repo.get(db, id_val, "product_id")

    def create(self, db: Session, data: dict):
        if not category_repo.get(db, data["category_id"], "category_id"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot assign product to non-existent category",
            )
        return product_repo.create(db, data)

    def update(self, db: Session, obj, data: dict):
        return product_repo.update(db, obj, data)

    def delete(self, db: Session, obj):
        product_repo.delete(db, obj)


product_service = ProductService()
