from fastapi import APIRouter


router = APIRouter()


@router.get('/')
def print() -> str:

    return "Hi"

