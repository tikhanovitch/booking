from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, PositiveInt, Field

app = FastAPI()


class User(BaseModel):
    item_id: PositiveInt
    age: int = Field(default=18, gt=0, lt=120)
    name: str = "John"
    surname: str = "Doe"
    email: EmailStr


@app.get("/items/{item_id}/{name}")
def get_pass_params(item_id: int, name: str) -> dict:
    return {"item_id": item_id, "name": name}


@app.get("/items")
def get_querry_params(item_id: int, name: str) -> dict:
    return {"item_id": item_id, "name": name}


@app.get("/items/{item_id}")
def get_querry_pass_params(item_id: int, name: str) -> dict:
    return {"item_id": item_id, "name": name}


@app.post("/users", response_model=User)
def get_user() -> User:
    # import pdb; pdb.set_trace()
    user_db = {
        "item_id": 111,
        "age": 25,
        "name": "Jane",
        "surname": "Doe",
        "email": "Jane.Doe@example.com"
    }
    user = User(**user_db)
    return user
