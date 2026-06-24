from datetime import datetime

from pydantic import BaseModel


class FlareBase(BaseModel):
    flare_id: str
    flare_class: str
    start_time: datetime
    peak_time: datetime | None
    end_time: datetime | None
    source_location: str | None
    active_region_num: int | None
    note: str | None
    link: str | None


class FlareResponse(FlareBase):
    id: int

    model_config = {'from_attributes': True}
