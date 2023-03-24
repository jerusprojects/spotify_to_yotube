from .config import settings

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(settings.DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()