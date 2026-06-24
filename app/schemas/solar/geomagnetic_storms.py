from datetime import datetime

from pydantic import BaseModel


class GeomagneticStormBase(BaseModel):
    gst_id: str
    start_time: datetime
    kp_index_max: float | None
    link: str | None


class GeomagneticStormResponse(GeomagneticStormBase):
    id: int

    model_config = {'from_attributes': True}
