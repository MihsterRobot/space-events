from datetime import datetime

from pydantic import BaseModel


class LaunchBase(BaseModel):
    launch_id: str
    launch_site: str
    name: str
    launch_date: datetime
    status: str
    rocket_name: str
    rocket_type: str
    mission_name: str | None
    mission_description: str | None
    is_crewed: bool
    serial_number: str | None


class LaunchResponse(LaunchBase):
    id: int

    model_config = {'from_attributes': True}
