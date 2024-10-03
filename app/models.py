from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    year = Column(Integer)
    selling_price = Column(Integer)
    km_driven = Column(Integer)
    fuel = Column(String)
    seller_type = Column(String)
    transmission = Column(String)
    owner = Column(String)
    mileage = Column(String)
    engine = Column(String)
    max_power = Column(String)
    torque = Column(String)
    seats = Column(Float)
