import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

ca_path = os.path.join(os.path.dirname(__file__), "ca.pem")

engine = create_engine(
    DB_URL,
    connect_args={
        "ssl": {
            "ca": ca_path
        }
    },
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()