from fastapi import APIRouter

router = APIRouter()

@router.get("/requests")
def get_purchase_requests():
    return {
        "message": "Purchase requests retrieved",
        "data": []
    }
