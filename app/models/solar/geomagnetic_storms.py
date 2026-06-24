from sqlalchemy import Column, Integer, Float, String, DateTime

from app.db.session import Base


class GeomagneticStorm(Base):
    __tablename__ = 'geomagnetic_storms'

    id = Column(Integer, primary_key=True)
    gst_id = Column(String, unique=True, nullable=False)
    start_time = Column(DateTime, nullable=False)
    kp_index_max = Column(Float, nullable=True)
    link = Column(String, nullable=True)
