from app.models.inventory_item import InventoryItem


class InventoryRepository:
    def list_items(self):
        return [
            InventoryItem(
                item_code="RM-1001",
                item_name="Steel Frame Component",
                quantity_available=125.0,
                warehouse_code="WH-01",
                unit_of_measure="pcs",
                description="Raw material for door and frame production",
            ),
            InventoryItem(
                item_code="RM-1002",
                item_name="Radiator Panel",
                quantity_available=80.0,
                warehouse_code="WH-02",
                unit_of_measure="pcs",
                description="Heating radiator production component",
            ),
        ]
