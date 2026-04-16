from fastapi import FastAPI
from app.api.routes import procurement, approvals, inventory

app = FastAPI(title="ERP Data Platform API")

app.include_router(procurement.router, prefix="/api/procurement", tags=["Procurement"])
app.include_router(approvals.router, prefix="/api/approvals", tags=["Approvals"])
app.include_router(inventory.router, prefix="/api/inventory", tags=["Inventory"])


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "erp-data-platform"}
