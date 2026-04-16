from app.models.approval import Approval


class ApprovalService:
    def process_approval(self, payload):
        approval = Approval(
            request_number=payload.request_number,
            approved_by_user_id=payload.approved_by_user_id,
            action=payload.action,
            comment=payload.comment,
        )

        return {
            "request_number": approval.request_number,
            "approved_by_user_id": approval.approved_by_user_id,
            "action": approval.action,
            "comment": approval.comment,
            "status": approval.status,
        }
