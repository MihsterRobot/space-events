from sqlalchemy import Column, Integer, String, DateTime

from app.db.session import Base


class Flare(Base):
    __tablename__ = 'flares'

    id = Column(Integer, primary_key=True)
    flare_id = Column(String, unique=True, nullable=False)
    flare_class = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    peak_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    source_location = Column(String, nullable=True)
    active_region_num = Column(Integer, nullable=True)
    note = Column(String, nullable=True)
    link = Column(String, nullable=True)
