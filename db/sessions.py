import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = os.getenv("DATABASE_URL", "sqlite:///./medicine_ordering.db")
engine = create_engine("mysql+pymysql://root:root%40123@localhost:3306/medordsysdb")
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
