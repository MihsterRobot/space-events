from datetime import datetime

from pydantic import BaseModel


class AsteroidBase(BaseModel):
    nasa_id: str
    name: str
    close_approach_date: datetime
    miss_distance_km: float
    relative_velocity_kmh: float
    is_potentially_hazardous: bool
    absolute_magnitude: float | None


class AsteroidResponse(AsteroidBase):
    id: int

    model_config = {'from_attributes': True}
