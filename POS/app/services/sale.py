from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List, Optional
from app.schemas.sales import SaleCreate
from app.models.sales import Sale
from app.models.sale_items import SaleItem
from app.repositories.users import user_repo
from app.repositories.sale import sale_repo
from app.repositories.products import product_repo
from app.repositories.customers import customer_repo


class SaleService:
    def get_all_sales(self, db: Session, skip: int = 0, limit: int = 100) -> List[Sale]:
        return sale_repo.get_all(db, skip=skip, limit=limit)

    def get_sale_by_id(self, db: Session, sale_id: int) -> Sale:
        sale = sale_repo.get_by_id(db, sale_id)
        if not sale:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Sale not found"
            )
        return sale

    def process_sale(
        self, db: Session, sale_data: SaleCreate, user_id: Optional[int] = None
    ) -> Sale:
        user = user_repo.get_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )

        if sale_data.customer_id is not None and not customer_repo.get(
            db, sale_data.customer_id, "id"
        ):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
            )

        total = 0.0
        try:
            sale = Sale(
                user_id=user_id,
                total_amount=0.0,
                customer_id=sale_data.customer_id,
                payment_method=sale_data.payment_method,
            )
            db.add(sale)
            db.flush()

            for item_in in sale_data.items:
                product = product_repo.get_by_id(db, item_in.product_id)
                if not product:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Product {item_in.product_id} not found",
                    )
                if product.quantity < item_in.quantity:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Insufficient stock for {product.name}",
                    )

                product.quantity -= item_in.quantity
                item_total = item_in.quantity * product.price
                total += float(item_total)

                db.add(
                    SaleItem(
                        sale_id=sale.sale_id,
                        product_id=product.product_id,
                        quantity=item_in.quantity,
                        unit_price=product.price,
                        subtotal=item_total,
                    )
                )

            sale.total_amount = total
            db.commit()
            db.refresh(sale)
            return sale
        except Exception:
            db.rollback()
            raise


sale_service = SaleService()
