from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.sales import SaleCreate, SaleResponse
from app.services.sale import sale_service
from app.services.dependencies import get_current_user
from app.models.users import User

router = APIRouter(prefix="/sales", tags=["sales"])


@router.post("", response_model=SaleResponse, status_code=status.HTTP_201_CREATED)
@router.post(
    "/",
    response_model=SaleResponse,
    status_code=status.HTTP_201_CREATED,
    include_in_schema=False,
)
def create_sale(
    sale_data: SaleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return sale_service.process_sale(db, sale_data, user_id=current_user.user_id)


@router.get("", response_model=List[SaleResponse])
@router.get("/", response_model=List[SaleResponse], include_in_schema=False)
def get_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return sale_service.get_all_sales(db, skip=skip, limit=limit)


@router.get("/{sale_id}", response_model=SaleResponse)
def get_sale(sale_id: int, db: Session = Depends(get_db)):
    return sale_service.get_sale_by_id(db, sale_id)
