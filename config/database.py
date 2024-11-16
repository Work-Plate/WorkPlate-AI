from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config.secret import DATABASE_URL

engine = create_engine(
    DATABASE_URL
)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
