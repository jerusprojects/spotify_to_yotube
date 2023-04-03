from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base
from models.relations import yt_track_yt_playlist


class YtTrack(Base):
    __tablename__ = "yt_tracks"

    id = Column(Integer, primary_key=True)
    video_id = Column(String)
    title = Column(String)
    artists = Column(String)
    album = Column(String)
    duration = Column(String)
    thumbnails = Column(String)

    # yt_library = relationship("YtLibrary", back_populates="yt_library")
    yt_playlists = relationship(
        "YtPlaylist", secondary=yt_track_yt_playlist, back_populates="yt_tracks"
    )
