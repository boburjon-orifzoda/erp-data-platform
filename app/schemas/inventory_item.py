from pydantic import BaseModel
from typing import Optional


class InventoryItemResponse(BaseModel):
    item_code: str
    item_name: str
    quantity_available: float
    warehouse_code: str
    unit_of_measure: str
    description: Optional[str] = None
