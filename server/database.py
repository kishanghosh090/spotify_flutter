from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+psycopg://user:0088@localhost:5432/spotify"

engine = create_engine(DATABASE_URL)
SessonLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessonLocal()