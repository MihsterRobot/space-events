from datetime import datetime

from pydantic import BaseModel


class CoronalMassEjectionBase(BaseModel):
    cme_id: str
    cme_type: str | None
    start_time: datetime
    source_location: str | None
    active_region_num: int | None
    note: str | None
    link: str | None
    instruments: str | None
    speed: float | None
    latitude: float | None
    longitude: float | None
    half_angle: float | None


class CoronalMassEjectionResponse(CoronalMassEjectionBase):
    id: int

    model_config = {'from_attributes': True}
