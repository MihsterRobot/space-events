from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime

from app.db.session import Base


class Asteroid(Base):
    __tablename__ = 'asteroids'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    nasa_id = Column(String, unique=True, nullable=False)
    close_approach_date = Column(DateTime, nullable=False)
    miss_distance_km = Column(Float, nullable=False)
    relative_velocity_kmh = Column(Float, nullable=False)
    is_potentially_hazardous = Column(Boolean, nullable=False)
    absolute_magnitude = Column(Float, nullable=True)
