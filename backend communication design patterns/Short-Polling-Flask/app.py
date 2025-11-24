from flask import Flask, request
import threading
import time

jobs = {}
app = Flask(__name__)


@app.post("/submit")
def submit_job():
    job_id = f"job:{int(time.time() * 1000)}"
    jobs[job_id] = 0

    thread = threading.Thread(target=update_job, args=(job_id,))
    thread.start()

    return f"\n\n{job_id}\n\n", 200, {"Content-Type": "text/plain"}


@app.get("/checkstatus")
def check_status():
    job_id = request.args.get("jobId")
    progress = jobs.get(job_id, None)
    return f"\n\nJobStatus: {progress}%\n\n", 200, {"Content-Type": "text/plain"}


def update_job(job_id):
    for p in range(0, 101, 10):
        jobs[job_id] = p
        print(f"updated {job_id} to {p}")
        if p == 100:
            return
        time.sleep(3)


if __name__ == "__main__":
    # Flask uses Werkzeug’s built-in development WSGI server.
    app.run(port=8080)
