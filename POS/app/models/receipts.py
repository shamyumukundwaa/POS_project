from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Receipt(Base):
    __tablename__ = "receipts"

    receipt_id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.sale_id"), unique=True, nullable=False)
    issued_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    receipt_number = Column(String, nullable=False, unique=True, index=True)

    sale = relationship("Sale", back_populates="receipt")
