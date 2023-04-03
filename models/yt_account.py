from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base


class YtAccount(Base):
    __tablename__ = "yt_accounts"

    id = Column(Integer, primary_key=True)
    header_auth = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    user = relationship("User", back_populates="yt_account")
    yt_playlists = relationship("YtPlaylist", backref="yt_account")
