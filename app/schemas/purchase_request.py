from pydantic import BaseModel
from typing import Optional


class PurchaseRequestCreate(BaseModel):
    request_number: str
    department_id: int
    requested_by_user_id: int
    total_amount: float
    currency_code: str
    vendor_id: Optional[int] = None
    description: Optional[str] = None


class PurchaseRequestResponse(BaseModel):
    request_number: str
    department_id: int
    requested_by_user_id: int
    total_amount: float
    currency_code: str
    status: str
    vendor_id: Optional[int] = None
    description: Optional[str] = None
