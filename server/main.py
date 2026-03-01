import uuid
import bcrypt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import UUID, VARCHAR, Column, LargeBinary, create_engine
from sqlalchemy.orm import sessionmaker
import uvicorn
from sqlalchemy.ext.declarative import declarative_base

app = FastAPI()

DATABASE_URL = "postgresql+psycopg://user:0088@localhost:5432/spotify"

engine = create_engine(DATABASE_URL)
SessonLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessonLocal()

Base = declarative_base()

# database model for user create schema and user table in database
class User(Base):
    __tablename__ = "users"
    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    username = Column(VARCHAR(100), unique=True, index=True)
    email = Column(VARCHAR(100), unique=True, index=True)
    password = Column(LargeBinary, nullable=False)

Base.metadata.create_all(bind=engine)

# base model for user creation(route request body)
class UserCreate(BaseModel):
    username: str
    password: str
    email: str


@app.post("/signup")
async def signup(user: UserCreate):

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

if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8000)