# app.py - FastAPI version of long polling (single file)
# ------------------------------------------------------
# This mirrors the same Node.js logic but using async/await.
# - /submit: returns jobId and starts background async updater
# - /checkstatus: long-polls using await until job reaches 100%

from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse
import asyncio
import time

app = FastAPI()

# Job dictionary (same as Node.js)
jobs = {}


@app.post("/submit", response_class=PlainTextResponse)
async def submit():
    # Create jobId similar to Node.js
    job_id = f"job:{int(time.time() * 1000)}"
    jobs[job_id] = 0

    # Fire async background task
    asyncio.create_task(update_job(job_id, 0))

    return f"\n\n{job_id}\n\n"


@app.get("/checkstatus", response_class=PlainTextResponse)
async def check_status(jobId: str = Query(...)):
    # Long polling: keep awaiting until complete
    while not await check_job_complete(jobId):
        await asyncio.sleep(1)  # same 1 sec wait loop

    return f"\n\nJobStatus: Complete {jobs[jobId]}%\n\n"


async def update_job(job_id: str, progress: int):
    """Async version of updateJob() from Node.js."""
    while progress <= 100:
        jobs[job_id] = progress
        print(f"updated {job_id} to {progress}")

        if progress == 100:
            return

        await asyncio.sleep(10)  # same 10 sec interval
        progress += 10


async def check_job_complete(job_id):
    """Async version of checkJobComplete() in Node.js."""
    return jobs.get(job_id, 0) >= 100
