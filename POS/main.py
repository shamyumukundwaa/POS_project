import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import database

from app.models.category import Category
from app.models.suppliers import Supplier
from app.models.products import Product
from app.models.customers import Customer
from app.models.users import User
from app.models.sales import Sale
from app.models.sale_items import SaleItem
from app.models.payments import Payment
from app.models.receipts import Receipt

logger = logging.getLogger(__name__)
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Coffee Shop POS REST API Engine",
    description="Layered clean architecture handling single-outlet transaction checkpoints.",
    version="1.0.0",
)


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception for %s", request.url.path)
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})


from app.routers import (
    category,
    products,
    sale,
    users,
    customers,
    suppliers,
    payments,
    receipts,
)

app.include_router(category.router)
app.include_router(products.router)
app.include_router(sale.router)
app.include_router(users.router)
app.include_router(customers.router)
app.include_router(suppliers.router)
app.include_router(payments.router)
app.include_router(receipts.router)


@app.get("/", tags=["Heartbeat"])
def system_check():
    return {
        "status": "online",
        "message": "Coffee shop Till endpoint layer is running perfectly",
    }
