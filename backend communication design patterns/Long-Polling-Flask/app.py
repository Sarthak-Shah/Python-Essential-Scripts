# app.py - Flask version of long polling (single file)
# -----------------------------------------------
# This mimics your Express.js long-polling code exactly.
# - /submit creates a job and starts progress update thread
# - /checkstatus blocks (long polling) until job reaches 100%

from flask import Flask, request
import time
import threading

app = Flask(__name__)

# In-memory job storage (same as Node.js)
jobs = {}


@app.post("/submit")
def submit():
    # Create a job ID like Node.js: job:timestamp
    job_id = f"job:{int(time.time() * 1000)}"
    jobs[job_id] = 0

    # Start background thread to update job
    thread = threading.Thread(target=update_job, args=(job_id, 0))
    thread.start()

    return f"\n\n{job_id}\n\n", 200, {"Content-Type": "text/plain"}


@app.get("/checkstatus")
def check_status():
    job_id = request.args.get("jobId")

    # Long polling: block until job complete
    while not check_job_complete(job_id):
        time.sleep(1)  # same 1 sec wait loop as Node.js long polling

    return f"\n\nJobStatus: Complete {jobs[job_id]}%\n\n", 200, {"Content-Type": "text/plain"}


def update_job(job_id, progress):
    """Mimics the async updateJob() in your Node.js example."""
    while progress <= 100:
        jobs[job_id] = progress
        print(f"updated {job_id} to {progress}")

        if progress == 100:
            return

        time.sleep(5)  # same 10 sec interval as Node.js
        progress += 10


def check_job_complete(job_id):
    """Equivalent to async checkJobComplete() in Node.js."""
    # return True only when job progress is 100%
    return jobs.get(job_id, 0) >= 100


if __name__ == "__main__":
    app.run(port=8080)
