from pydantic import BaseModel, Field


class YtTrack(BaseModel):
    yt_track_id: int = Field(...)
    video_id: str = Field(...)
    title: str = Field(...)
    artists: str = Field(...)
    album: str = Field(...)
    duration: str = Field(...)
    thumbnails: str = Field(...)
