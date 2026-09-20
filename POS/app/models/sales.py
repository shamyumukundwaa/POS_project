from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Sale(Base):
    __tablename__ = "sales"

    sale_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    total_amount = Column(Float, nullable=False, default=0.0)
    payment_method = Column(String, default="cash")
    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="sales")
    sale_items = relationship("SaleItem", back_populates="sale")
    payments = relationship("Payment", back_populates="sale")
    receipt = relationship("Receipt", back_populates="sale", uselist=False)
    