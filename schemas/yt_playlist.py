from pydantic import BaseModel, Field

from schemas.yt_account import YtAccountBase


class YtPlaylist(BaseModel):
    yt_playlist_id: int = Field(...)
    privacy: str = Field(...)
    title: str = Field(...)
    thumbnails: str = Field(...)
    description: str = Field(...)
    author: str = Field(...)
    year: str = Field(...)
    duration: str = Field(...)
    track_count: int = Field(...)
    yt_account: YtAccountBase = Field(...)
