from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse
import asyncio

app = FastAPI()
jobs = {}  # in-memory dictionary, same as Node.js example


@app.post("/submit", response_class=PlainTextResponse)
async def submit_job():
    job_id = f"job:{int(asyncio.get_event_loop().time()*1000)}"
    jobs[job_id] = 0
    asyncio.create_task(update_job(job_id))   # background job
    return f"\n\n{job_id}\n\n"


@app.get("/checkstatus", response_class=PlainTextResponse)
async def check_status(jobId: str = Query(...)):
    progress = jobs.get(jobId, None)
    return f"\n\nJobStatus: {progress}%\n\n"


async def update_job(job_id):
    for p in range(0, 101, 10):
        jobs[job_id] = p
        print(f"updated {job_id} to {p}")
        if p == 100:
            return
        await asyncio.sleep(3)  # same 3-second interval
