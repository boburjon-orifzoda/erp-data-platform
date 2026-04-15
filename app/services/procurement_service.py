from app.models.purchase_request import PurchaseRequest


class ProcurementService:
    def create_purchase_request(self, payload):
        purchase_request = PurchaseRequest(
            request_number=payload.request_number,
            department_id=payload.department_id,
            requested_by_user_id=payload.requested_by_user_id,
            total_amount=payload.total_amount,
            currency_code=payload.currency_code,
            vendor_id=payload.vendor_id,
            description=payload.description,
        )

        return {
            "request_number": purchase_request.request_number,
            "department_id": purchase_request.department_id,
            "requested_by_user_id": purchase_request.requested_by_user_id,
            "total_amount": purchase_request.total_amount,
            "currency_code": purchase_request.currency_code,
            "status": purchase_request.status,
            "vendor_id": purchase_request.vendor_id,
            "description": purchase_request.description,
        }
