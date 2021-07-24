from fastapi import APIRouter

router = APIRouter()

# /users

@router.get("/")
async def get_ursers():
    return {"message": "Get Users!"}

