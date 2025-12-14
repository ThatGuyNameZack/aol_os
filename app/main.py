from fastapi import FastAPI
from app.version_a import router as version_a
from app.version_b import router as version_b
from app.metrics import router as metrics_router

app = FastAPI(title="OS Concurrency Demo")

app.include_router(version_a, prefix="/v1")
app.include_router(version_b, prefix="/v2")
app.include_router(metrics_router)

@app.get("/")
def root():
    return {"message": "OS Concurrency Project Running"}
