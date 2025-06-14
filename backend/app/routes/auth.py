from fastapi import APIRouter

router = APIRouter()

@router.get("/whoami")
def auth_check():
    return {"user": "placeholder-user"}