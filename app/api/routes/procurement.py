from fastapi import APIRouter
from app.schemas.purchase_request import PurchaseRequestCreate, PurchaseRequestResponse
from app.services.procurement_service import ProcurementService

router = APIRouter()
procurement_service = ProcurementService()


@router.get("/requests")
def get_purchase_requests():
    return {
        "status": "success",
        "message": "Purchase requests retrieved",
        "data": []
    }


@router.post("/requests")
def create_purchase_request(payload: PurchaseRequestCreate):
    result = procurement_service.create_purchase_request(payload)
    return {
        "status": "success",
        "message": "Purchase request created",
        "data": result
    }
