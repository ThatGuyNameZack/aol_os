from fastapi import FastAPI
import asyncio
from app.metrics import router as metrics_router

app = FastAPI()

app.include_router(metrics_router)  # THIS IS REQUIRED

shared_counter = 0
lock = asyncio.Lock()

@app.get("/task")
async def run_task():
    global shared_counter

    async with lock:
        temp = shared_counter
        await asyncio.sleep(0.1)
        shared_counter = temp + 1

    await asyncio.sleep(1)
    return {
        "status": "done",
        "version": "B",
        "counter": shared_counter
    }
