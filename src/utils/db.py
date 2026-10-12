from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.settings import settings

Base = declarative_base()

engine = create_engine(settings.DB_CONNECTION)

Local_session = sessionmaker(bind=engine)


def get_db():
    session = Local_session()
    try:
        yield session
    finally:
        session.close()