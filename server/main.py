from fastapi import FastAPI
import uvicorn
from models.base import Base
from routes import auth
from database import engine


app = FastAPI()




app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])

Base.metadata.create_all(bind=engine)





if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8000)