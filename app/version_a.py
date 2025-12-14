# single threaded

from fastapi import APIRouter
import time

router = APIRouter()

@router.get("/task")
def run_task():
    time.sleep(1)  # simulate CPU work
    return {"status": "done", "version": "A"}
