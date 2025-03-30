from sqlmodel import Field

from utils.common_models import BaseModel


class ShortenedUrl(BaseModel, table=True):
    id: int | None = Field(primary_key=True)
    main_url: str = Field()
    short_url: str = Field(index=True)
    active: bool = Field(default=True)
    expired: bool = Field(default=False)
    visits: int = Field(default=0)
    last_usage: float = Field()
    expires_at: float | None = Field()
