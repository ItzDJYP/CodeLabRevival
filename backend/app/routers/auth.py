"""
Authentication router — POST /auth/login
Returns a JWT access token.
"""
import os
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, HTTPException, status
from jose import jwt

from app.data import get_user_by_email, verify_password, USERS, pwd_context
from app.models import LoginRequest, RegisterRequest, TokenResponse, UserPublic

router = APIRouter(prefix="/auth", tags=["auth"])

SECRET_KEY = os.getenv("SECRET_KEY", "changeme-use-env-var-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 8  # 8 hours


def _create_token(user_id: int, role: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": str(user_id), "role": role, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


@router.post("/login", response_model=TokenResponse)
def login(body: LoginRequest):
    user = get_user_by_email(body.email)
    if not user or not verify_password(body.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
        )
    token = _create_token(user["id"], user["role"])
    return TokenResponse(
        access_token=token,
        token_type="bearer",
        user=UserPublic(
            id=str(user["id"]),
            name=user["name"],
            email=user["email"],
            role=user["role"],
        ),
    )


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register(body: RegisterRequest):
    if body.role not in ("student", "instructor"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Role must be 'student' or 'instructor'.",
        )
    if get_user_by_email(body.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with that email already exists.",
        )
    new_id = max(u["id"] for u in USERS) + 1
    new_user = {
        "id": new_id,
        "name": body.name.strip(),
        "email": body.email.strip().lower(),
        "hashed_password": pwd_context.hash(body.password),
        "role": body.role,
    }
    USERS.append(new_user)
    token = _create_token(new_id, body.role)
    return TokenResponse(
        access_token=token,
        token_type="bearer",
        user=UserPublic(
            id=str(new_id),
            name=new_user["name"],
            email=new_user["email"],
            role=new_user["role"],
        ),
    )
