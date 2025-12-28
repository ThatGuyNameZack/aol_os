from fastapi import FastAPI
import time
from app.metrics import router as metrics_router

app = FastAPI()

app.include_router(metrics_router)  # THIS IS REQUIRED

def busy_wait(seconds):
    end = time.time() + seconds
    while time.time() < end:
        pass

@app.get("/task")
def run_task():
    busy_wait(1)
    return {"status": "done", "version": "A"}
