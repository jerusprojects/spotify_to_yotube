from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base
from models.relations import yt_track_yt_playlist


class YtPlaylist(Base):
    __tablename__ = "yt_playlists"

    id = Column(Integer, primary_key=True)
    privacy = Column(String)
    title = Column(String)
    thumbnails = Column(String)
    description = Column(String)
    author = Column(String)
    year = Column(String)
    duration = Column(String)
    trackCount = Column(Integer)
    yt_account_id = Column(Integer, ForeignKey("yt_accounts.id"))

    yt_tracks = relationship(
        "YtTrack", secondary=yt_track_yt_playlist, back_populates="yt_playlists"
    )
