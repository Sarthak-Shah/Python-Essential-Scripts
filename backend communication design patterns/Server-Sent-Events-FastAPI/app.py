"""
Server-Sent Events (SSE) demo using FastAPI
-------------------------------------------

Client-side code:
----------------------------------------
    let sse = new EventSource("http://localhost:8000/stream");
    sse.onmessage = console.log;

Run this file:
--------------
    uvicorn app:app --reload

Then open your browser console at:
    http://localhost:8000/

You’ll see continuous messages streamed from the server.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

# 👇 Add this block to allow requests from any origin (for dev purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to ["http://127.0.0.1:8000"] if needed
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root endpoint just returns a simple "hello!" message
@app.get("/")
async def home():
    return HTMLResponse("<h1>Hello!</h1><p>Open /stream to see SSE in action.</p>")


# Generator function that yields SSE messages
def event_stream():
    """
    This generator continuously yields data in SSE format.
    SSE requires each message to be prefixed with 'data:' and
    terminated with *two* newlines (\n\n).
    """
    i = 0
    while True:
        # Construct the SSE message
        message = f"data: hello from server ---- [{i}]\n\n"
        yield message

        i += 1
        # Sleep for 1 second before sending the next message
        time.sleep(1)


@app.get("/stream")
async def stream():
    """
    SSE endpoint:
    - Sets the correct Content-Type: text/event-stream
    - Uses StreamingResponse to continuously push data
    """
    return StreamingResponse(event_stream(), media_type="text/event-stream")

# Run with: uvicorn app:app --reload
# Default port is 8000, but you can change with --port option
