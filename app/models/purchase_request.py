class PurchaseRequest:
    def __init__(
        self,
        request_number: str,
        department_id: int,
        requested_by_user_id: int,
        total_amount: float,
        currency_code: str,
        status: str = "draft",
        vendor_id: int | None = None,
        description: str | None = None,
    ):
        self.request_number = request_number
        self.department_id = department_id
        self.requested_by_user_id = requested_by_user_id
        self.total_amount = total_amount
        self.currency_code = currency_code
        self.status = status
        self.vendor_id = vendor_id
        self.description = description
