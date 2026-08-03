from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    email = Column(String, nullable=True)
    loyalty_points = Column(Integer, default=0, nullable=True)

    sales = relationship("Sale", back_populates="customer")
