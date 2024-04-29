from pydantic import BaseModel, EmailStr, PositiveInt, Field


class User(BaseModel):
    id: PositiveInt
    age: int = Field(default=18, gt=0, lt=120)
    first_name: str = "John"
    second_name: str = "Doe"
    username: str = "username"
    email: EmailStr
