from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    hashed_password = Column(String)

    yt_account = relationship("YtAccount", uselist=False, back_populates="user")
