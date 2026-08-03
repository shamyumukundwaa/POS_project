from typing import Generic, Type, TypeVar, List, Optional
from sqlalchemy.orm import Session
from database import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def create(self, db: Session, obj_in_data: dict) -> ModelType:
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(
        self, db: Session, id_value: int, id_field_name: str
    ) -> Optional[ModelType]:
        id_attr = getattr(self.model, id_field_name)
        return db.query(self.model).filter(id_attr == id_value).first()

    def get_multi(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def update(self, db: Session, db_obj: ModelType, obj_in_data: dict) -> ModelType:
        for field, value in obj_in_data.items():
            if value is None:
                continue
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: ModelType) -> None:
        db.delete(db_obj)
        db.commit()
