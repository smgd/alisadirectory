from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker


def get_db_engine():
    created_engine = create_engine(DATABASE_URI, pool_pre_ping=True)
    if not database_exists(created_engine.url):
        create_database(created_engine.url)

    return created_engine


engine = get_db_engine()

Base = declarative_base()
Base.metadata.create_all(engine)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
