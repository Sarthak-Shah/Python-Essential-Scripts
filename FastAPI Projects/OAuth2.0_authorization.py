import os

from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth

"""
OAuth 2.0 Authorization Code Flow (FastAPI Implementation)
1️⃣ User Requests Authorization
User clicks Login (/login).
App redirects user to Google OAuth Authorization URL.
Google asks for user consent & permissions (scopes).

2️⃣ User Grants Permission & Redirects Back
After login, Google redirects back with an Authorization Code.
This code is temporary and must be exchanged for an Access Token.

3️⃣ Exchange Authorization Code for Access Token
The backend sends the Authorization Code to Google’s token endpoint.
Google verifies the request and responds with:
Access Token (used for API requests).
ID Token (JWT containing user identity details).

4️⃣ Retrieve User Information
The backend uses the Access Token to fetch user details.
This is done via Google’s UserInfo API.
The user’s email, name, and profile info are retrieved.

5️⃣ Use Access Token for API Authorization
The Access Token is used for subsequent API calls to protected resources.
If the token expires, the Refresh Token is used to obtain a new one.

6️⃣ Secure API Access
Validate the JWT Token Signature to ensure authenticity.
Enforce OAuth Scopes (e.g., allow read-only or admin access).
Implement Role-Based Access Control (RBAC) for authorization.

7️⃣ User Logs Out / Revokes Access
When logging out, clear session data and revoke the access token.
Ensure tokens are not stored insecurely (e.g., avoid local storage in frontend apps).
"""

app = FastAPI()

# Add SessionMiddleware with a secret key
app.add_middleware(SessionMiddleware, secret_key="top_secret")

# OAuth configuration
oauth = OAuth()
oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    access_token_url="https://oauth2.googleapis.com/token",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)


@app.get("/")
def home():
    return {"message": "Welcome! Click /login to authenticate."}


@app.get("/login")
async def login(request: Request):
    return await oauth.google.authorize_redirect(request, redirect_uri="http://localhost:8001/callback")


@app.get("/callback")
async def callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = token.get("userinfo")
    return {"message": f"Hello, {user['email']}!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8001)
