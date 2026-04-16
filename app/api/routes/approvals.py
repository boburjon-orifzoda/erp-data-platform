from fastapi import APIRouter
from app.schemas.approval import ApprovalActionRequest, ApprovalActionResponse
from app.services.approval_service import ApprovalService

router = APIRouter()
approval_service = ApprovalService()


@router.post("/action", response_model=ApprovalActionResponse)
def process_approval(payload: ApprovalActionRequest):
    return approval_service.process_approval(payload)
