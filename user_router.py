from fastapi import APIRouter, Depends

from dependencies.authentication import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
def current_user(current_user: dict = Depends(get_current_user)):
    return {
        "username": current_user["username"],
        "role": current_user["role"],
        "is_active": current_user["is_active"],
    }
