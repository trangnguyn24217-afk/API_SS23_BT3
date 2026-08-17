from fastapi import APIRouter, HTTPException, status

from schemas.schemas import LoginRequest, TokenResponse
from services.auth_service import authenticate, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest):
    user = authenticate(data.username, data.password)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    if not user["is_active"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive",
        )

    return {
        "access_token": create_access_token(user),
        "token_type": "bearer",
    }
