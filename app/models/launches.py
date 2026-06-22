from sqlalchemy import Column, Integer, String, DateTime, Boolean

from app.db.session import Base


class Launch(Base):
    __tablename__ = 'launches'

    id = Column(Integer, primary_key=True)
    launch_id = Column(String, unique=True, nullable=False)
    launch_site = Column(String, nullable=False)
    name = Column(String, nullable=False)
    launch_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)
    rocket_name = Column(String, nullable=False)
    rocket_type = Column(String, nullable=False)
    mission_name = Column(String, nullable=True)
    mission_description = Column(String, nullable=True)
    is_crewed = Column(Boolean, nullable=False)
    serial_number = Column(String, nullable=True)
    