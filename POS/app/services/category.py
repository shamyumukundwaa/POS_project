from sqlalchemy.orm import Session
from app.repositories.category import category_repo


class CategoryService:
    def get_all(self, db: Session):
        return category_repo.get_multi(db)

    def get_by_id(self, db: Session, id_val: int):
        return category_repo.get(db, id_val, "category_id")

    def create(self, db: Session, data: dict):
        return category_repo.create(db, data)

    def update(self, db: Session, obj, data: dict):
        return category_repo.update(db, obj, data)

    def delete(self, db: Session, obj):
        category_repo.delete(db, obj)


category_service = CategoryService()
