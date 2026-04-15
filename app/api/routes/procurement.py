from fastapi import APIRouter
from app.schemas.purchase_request import PurchaseRequestCreate, PurchaseRequestResponse
from app.services.procurement_service import ProcurementService

router = APIRouter()
procurement_service = ProcurementService()


@router.get("/requests")
def get_purchase_requests():
    return {
        "message": "Purchase requests retrieved",
        "data": []
    }


@router.post("/requests", response_model=PurchaseRequestResponse)
def create_purchase_request(payload: PurchaseRequestCreate):
    return procurement_service.create_purchase_request(payload)
