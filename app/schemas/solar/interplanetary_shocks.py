from datetime import datetime

from pydantic import BaseModel


class InterplanetaryShockBase(BaseModel):
    ips_id: str
    event_time: datetime
    location: str | None
    instruments: str | None
    link: str | None


class InterplanetaryShockResponse(InterplanetaryShockBase):
    id: int

    model_config = {'from_attributes': True}
    