from fastapi import FastAPI
from app.api.routes import procurement

app = FastAPI(title="ERP Data Platform API")

app.include_router(procurement.router, prefix="/api/procurement", tags=["Procurement"])

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "erp-data-platform"}
