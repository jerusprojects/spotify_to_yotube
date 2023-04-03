from sqlalchemy import Column, ForeignKey, Table

from config.database import Base

yt_track_yt_playlist = Table(
    "yt_track_yt_playlist",
    Base.metadata,
    Column("yt_track_id", ForeignKey("yt_tracks.id"), primary_key=True),
    Column("yt_playlist_id", ForeignKey("yt_playlists.id"), primary_key=True),
)
