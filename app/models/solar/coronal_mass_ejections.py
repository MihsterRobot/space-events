from sqlalchemy import Column, Integer, String, Float, DateTime

from app.db.session import Base


class CoronalMassEjection(Base):
    __tablename__ = 'coronal_mass_ejections'

    id = Column(Integer, primary_key=True)
    cme_id = Column(String, unique=True, nullable=False)
    cme_type = Column(String, nullable=True)
    start_time = Column(DateTime, nullable=False)
    source_location = Column(String, nullable=True)
    active_region_num = Column(Integer, nullable=True)
    note = Column(String, nullable=True)
    link = Column(String, nullable=True)
    instruments = Column(String, nullable=True)
    speed = Column(Float, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    half_angle = Column(Float, nullable=True)
