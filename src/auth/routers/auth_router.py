from fastapi import APIRouter

from src.auth.schemas.user_schema import User

router = APIRouter(
    prefix="/users",
    tags=["Auth"]
)


@router.post("", response_model=User)
def get_user() -> User:
    # import pdb; pdb.set_trace()
    user_db = {
        "id": 111,
        "age": 25,
        "name": "Jane",
        "surname": "Doe",
        "email": "Jane.Doe@example.com"
    }
    user = User(**user_db)
    return user
