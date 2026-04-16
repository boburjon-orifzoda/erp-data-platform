from app.repositories.inventory_repository import InventoryRepository


class InventoryService:
    def __init__(self):
        self.repository = InventoryRepository()

    def get_inventory_items(self):
        items = self.repository.list_items()
        return [
            {
                "item_code": item.item_code,
                "item_name": item.item_name,
                "quantity_available": item.quantity_available,
                "warehouse_code": item.warehouse_code,
                "unit_of_measure": item.unit_of_measure,
                "description": item.description,
            }
            for item in items
        ]
