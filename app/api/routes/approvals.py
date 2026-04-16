from fastapi import APIRouter
from app.schemas.approval import ApprovalActionRequest
from app.services.approval_service import ApprovalService

router = APIRouter()
approval_service = ApprovalService()


@router.post("/action")
def process_approval(payload: ApprovalActionRequest):
    result = approval_service.process_approval(payload)
    return {
        "status": "success",
        "message": "Approval action processed",
        "data": result
    }
