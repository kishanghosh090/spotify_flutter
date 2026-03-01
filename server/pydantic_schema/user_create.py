from pydantic import BaseModel


# base model for user creation(route request body)
class UserCreate(BaseModel):
    username: str
    password: str
    email: str