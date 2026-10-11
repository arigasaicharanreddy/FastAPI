from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.settings import Settings


Base = declarative_base() 

engine = create_engine(url = Settings.DB_CONNECTION)
Local_session = sessionmaker(bind = engine)

def get_db():
    session = Local_session()
    try : 
        yield session
    finally : 
        session.close()