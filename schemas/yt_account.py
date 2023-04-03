from pydantic import BaseModel, Field

from schemas.user import User


class YtAccountBase(BaseModel):
    yt_account_base_id: int = Field(...)
    user: User = Field(...)


class YtAccountLogin(YtAccountBase):
    header_auth: str = Field(...)
