from pydantic import BaseModel
from typing import Optional


class ApprovalActionRequest(BaseModel):
    request_number: str
    approved_by_user_id: int
    action: str
    comment: Optional[str] = None


class ApprovalActionResponse(BaseModel):
    request_number: str
    approved_by_user_id: int
    action: str
    comment: Optional[str] = None
    status: str
