#multi threading

from fastapi import APIRouter
import asyncio

router = APIRouter()

shared_counter = 0
lock = asyncio.Lock()

@router.get("/task")
async def run_task():
    global shared_counter

    async with lock:  # mutex
        temp = shared_counter
        await asyncio.sleep(0.1)
        shared_counter = temp + 1

    await asyncio.sleep(1)
    return {
        "status": "done",
        "version": "B",
        "counter": shared_counter
    }
