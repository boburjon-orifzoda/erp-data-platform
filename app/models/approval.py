class Approval:
    def __init__(
        self,
        request_number: str,
        approved_by_user_id: int,
        action: str,
        status: str = "processed",
        comment: str | None = None,
    ):
        self.request_number = request_number
        self.approved_by_user_id = approved_by_user_id
        self.action = action
        self.status = status
        self.comment = comment
