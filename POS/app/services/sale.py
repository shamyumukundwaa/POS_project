import uuid
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.sale import sale_repo
from app.repositories.products import product_repo
from app.repositories.users import user_repo
from app.repositories.customers import customer_repo
from app.models.sale_items import SaleItem
from app.models.receipts import Receipt
from app.schemas.sales import  SaleCreate


class SaleService:
    def process_checkout(self, db: Session, sale_in: SaleCreate):
        user = user_repo.get(db, id_value=sale_in.user_id, id_field_name="user_id")
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Staff member processing this sale does not exist",
            )

        if sale_in.customer_id:
            customer = customer_repo.get(
                db, id_value=sale_in.customer_id, id_field_name="customer_id"
            )
            if not customer:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Referenced customer profile does not exist",
                )
        db_sale = sale_repo.create(
            db,
            {
                "user_id": sale_in.user_id,
                "customer_id": sale_in.customer_id,
                "total_amount": 0,
            },
        )

        running_total = 0

        for item in sale_in.items:
            product = product_repo.get(
                db, id_value=item.product_id, id_field_name="product_id"
            )
            if not product:
                db.rollback()
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Product with ID {item.product_id} does not exist",
                )

            if product.stock_quantity < item.quantity:
                db.rollback()
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Insufficient stock for {product.name}. Available: {product.stock_quantity}, Requested: {item.quantity}",
                )

           
            product.stock_quantity -= item.quantity

            item_subtotal = product.price * item.quantity
            running_total += item_subtotal

          
            db_item = SaleItem(
                sale_id=db_sale.sale_id,
                product_id=product.product_id,
                quantity=item.quantity,
                unit_price=product.price,
                subtotal=item_subtotal,
            )
            db.add(db_item)

        
        db_sale.total_amount = running_total

        db_receipt = Receipt(
            sale_id=db_sale.sale_id,
            receipt_number=f"REC-{uuid.uuid4().hex[:8].upper()}",
        )
        db.add(db_receipt)

        db.commit()
        db.refresh(db_sale)
        return db_sale


sale_service = SaleService()
