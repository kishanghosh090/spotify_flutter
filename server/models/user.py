import uuid
from sqlalchemy import TEXT, VARCHAR, Column, LargeBinary
from models.base import Base


# database model for user create schema and user table in database
class User(Base):
    __tablename__ = "users"
    id = Column(TEXT, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    username = Column(VARCHAR(100), unique=True, index=True)
    email = Column(VARCHAR(100), unique=True, index=True)
    password = Column(LargeBinary, nullable=False)
    