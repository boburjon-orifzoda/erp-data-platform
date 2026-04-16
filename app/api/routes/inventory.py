from fastapi import APIRouter
from app.services.inventory_service import InventoryService

router = APIRouter()
inventory_service = InventoryService()


@router.get("/items")
def get_inventory_items():
    return {
        "message": "Inventory items retrieved",
        "data": inventory_service.get_inventory_items()
    }
