from sqlalchemy import Column, Integer, String, DateTime

from app.db.session import Base


class InterplanetaryShock(Base):
    __tablename__ = 'interplanetary_shocks'

    id = Column(Integer, primary_key=True)
    ips_id = Column(String, unique=True, nullable=False)
    event_time = Column(DateTime, nullable=False)
    location = Column(String, nullable=True)
    instruments = Column(String, nullable=True)
    link = Column(String, nullable=True)
