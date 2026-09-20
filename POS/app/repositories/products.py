from sqlalchemy.orm import Session
from typing import Optional, List
from app.models.products import Product
from app.schemas.products import ProductCreate, ProductUpdate


class ProductRepository:
    def get_by_id(self, db: Session, product_id: int) -> Optional[Product]:
        return db.query(Product).filter(Product.product_id == product_id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[Product]:
        return db.query(Product).offset(skip).limit(limit).all()

    def get_by_sku(self, db: Session, sku: str) -> Optional[Product]:
        return db.query(Product).filter(Product.sku == sku).first()

    def create(self, db: Session, product_in: ProductCreate) -> Product:
        db_product = Product(
            name=product_in.name,
            price=product_in.price,
            quantity=product_in.quantity,
            category_id=product_in.category_id,
            sku=product_in.sku,
            supplier_id=product_in.supplier_id,
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    def update(
        self, db: Session, db_product: Product, update_data: ProductUpdate
    ) -> Product:
        for field, value in update_data.model_dump(exclude_unset=True).items():
            setattr(db_product, field, value)
        db.commit()
        db.refresh(db_product)
        return db_product

    def delete(self, db: Session, db_product: Product) -> None:
        db.delete(db_product)
        db.commit()


product_repo = ProductRepository()
