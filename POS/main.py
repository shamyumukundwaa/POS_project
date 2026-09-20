from fastapi import FastAPI
from app.routers import (
    products,
    users,
    category,
    customers,
    suppliers,
    sale,
    payments,
    receipts,
)

app = FastAPI(title="POS System")

app.include_router(users.router)
app.include_router(products.router)
app.include_router(category.router)
app.include_router(customers.router)
app.include_router(suppliers.router)
app.include_router(sale.router)
app.include_router(payments.router)
app.include_router(receipts.router)


@app.get("/")
def home():
    return {"message": "Welcome to the POS System"}
