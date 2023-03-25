from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

from .config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
