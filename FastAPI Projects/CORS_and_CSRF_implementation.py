""""""
"""
1) CORS (Cross-Origin Resource Sharing)
🧐 What is CORS?
- CORS is a security feature implemented by browsers to prevent JavaScript from making requests to a different domain.
- It blocks unauthorized requests from different origins unless explicitly allowed.

🎭 Analogy: A Strict Restaurant Policy
Imagine you visit McDonald's and try to use Burger King's seating area.
The Burger King manager (browser) blocks you unless McDonald's gives special permission.

Similarly, browsers block API requests from different domains unless the API explicitly allows them.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Allow frontend (React/Vue/Angular) to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://trusted-frontend.com"],  # Allow only specific frontend
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"]
)

@app.get("/data")
async def get_data():
    return {"message": "CORS is working!"}

"""
2) CSRF (Cross-Site Request Forgery)
🧐 What is CSRF?
CSRF is an attack where a hacker tricks a user into performing an unintended action on a trusted website.
The browser automatically includes authentication credentials (cookies, tokens), making the request appear legitimate.
🎭 Analogy: Fake Payment Request
1️⃣ You log into your bank account and keep the session open.
2️⃣ You visit a malicious website that secretly loads:
<img src="https://bank.com/transfer?amount=1000&to=hacker_account">
3️⃣ Your browser automatically sends authentication cookies, transferring money without your consent.
"""
#To prevent CSRF, we use CSRF tokens.
"""
Why Do We Need CSRF Tokens in Django?
Django automatically protects POST requests from CSRF attacks.
CSRF tokens ensure that only requests originating from your site are accepted.
The {% csrf_token %} tag helps insert the CSRF token in forms automatically.

🔹 Summary
Django CSRF Use Case	Solution
Forms in Templates	    {% csrf_token %} inside <form>
AJAX Requests	          Get CSRF token from <input name="csrfmiddlewaretoken">
JavaScript Fetch API	Extract CSRF token from cookies (csrftoken)
"""

from fastapi import FastAPI, Request, Depends, HTTPException

app = FastAPI()

# Dummy storage for CSRF tokens
CSRF_TOKENS = {}


def generate_csrf_token(user_id: str):
    """Generate and store CSRF token for a user."""
    import secrets
    token = secrets.token_hex(16)
    CSRF_TOKENS[user_id] = token
    return token


def verify_csrf_token(request: Request, token: str = None):
    """Verify CSRF token before processing sensitive actions."""
    user_id = "test_user"  # Assume we identify user by session (for example)
    if token is None or CSRF_TOKENS.get(user_id) != token:
        raise HTTPException(status_code=403, detail="CSRF Token Invalid")


@app.get("/csrf-token")
async def get_csrf_token():
    """Endpoint to get a CSRF token."""
    return {"csrf_token": generate_csrf_token("test_user")}


@app.post("/transfer-money")
async def transfer_money(request: Request, csrf_token: str = Depends(verify_csrf_token)):
    """Secure API endpoint requiring CSRF token."""
    return {"message": "Money transferred successfully!"}
