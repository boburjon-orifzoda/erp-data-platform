class InventoryItem:
    def __init__(
        self,
        item_code: str,
        item_name: str,
        quantity_available: float,
        warehouse_code: str,
        unit_of_measure: str,
        description: str | None = None,
    ):
        self.item_code = item_code
        self.item_name = item_name
        self.quantity_available = quantity_available
        self.warehouse_code = warehouse_code
        self.unit_of_measure = unit_of_measure
        self.description = description
