from fastapi import Depends, HTTPException
import bcrypt
from sqlalchemy.orm import Session

from models.user import User
from database import get_db
from pydantic_schema.user_create import UserCreate
from fastapi import APIRouter

router = APIRouter()

@router.post("/signup")
async def signup(user: UserCreate, db: Session = Depends(get_db)):

    if not user.username or not user.password or not user.email:
        raise HTTPException(status_code=400, detail="Username, password and email are required")
    
    existing_user = db.query(User).filter(User.email == user.email).first()
    print(existing_user)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
      

    new_user = User(
        username=user.username,
        email=user.email,
        password=bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user_id": str(new_user.id)}
