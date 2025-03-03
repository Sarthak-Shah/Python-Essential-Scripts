""""""
"""
pip install fastapi pyjwt passlib[bcrypt] python-multipart
1. fastapi → Web framework
2. pyjwt → JWT encoding & decoding
3. passlib[bcrypt] → Secure password hashing
4. python-multipart → Enables form data for login
"""

"""
1. ✅ Creates JWT (sub: username, exp: expiry time)
2. ✅ Decodes JWT & checks expiration
3. ✅ Returns username if valid, else errors out
"""

import jwt
from datetime import datetime, timedelta

# Secret key for signing JWT
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token valid for 30 minutes


def create_jwt_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    """Generate JWT token with expiration time."""
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})  # Set expiry
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_jwt_token(token: str):
    """Verify and decode JWT token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
        return username
    except jwt.ExpiredSignatureError:
        return "Token expired"
    except jwt.InvalidTokenError:
        return "Invalid token"


"""
1. ✅ Stores hashed passwords (bcrypt for security)
2. ✅ Validates user login
3. ✅ Issues JWT if credentials are correct
"""

from fastapi import FastAPI, HTTPException, Depends, Form
from passlib.context import CryptContext

app = FastAPI()

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Dummy user database
USER_DB = {
    "john": {"username": "john", "hashed_password": pwd_context.hash("pass123")}
}


def verify_password(plain_password, hashed_password):
    """Verify password with hashed version."""
    return pwd_context.verify(plain_password, hashed_password)


@app.post("/token")
async def login(username: str = Form(...), password: str = Form(...)):
    """Login endpoint that validates user and issues JWT token."""
    user = USER_DB.get(username)
    if not user or not verify_password(password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Generate JWT
    token = create_jwt_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}


"""
We use FastAPI Dependency Injection (Depends) to ensure JWT authentication before accessing protected routes.

1. ✅ Extracts user from JWT
2. ✅ Verifies token validity
3. ✅ Rejects unauthorized users
"""

from fastapi import Security
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Security(oauth2_scheme)):
    """Extracts and verifies the user from the JWT token."""
    user = verify_jwt_token(token)
    if user in ["Token expired", "Invalid token"]:
        raise HTTPException(status_code=401, detail=user)
    return user


@app.get("/protected")
async def protected_route(user: str = Depends(get_current_user)):
    """A protected route that requires JWT authentication."""
    return {"message": f"Hello {user}, you have access to this route!"}

"""
🛠 What Happens When a User Calls /protected?
1. FastAPI injects get_current_user() when calling /protected.
2. get_current_user() extracts the token from the request header.
3. It verifies the token using verify_jwt_token().
4. If valid, it returns the username → User is authenticated.
5. If invalid or expired, it raises 401 Unauthorized.
"""