from pydantic import BaseModel
from typing import List

class CarBase(BaseModel):
    name: str
    year: int
    selling_price: float
    km_driven: int
    fuel: str
    seller_type: str
    transmission: str
    owner: str
    mileage: str
    engine: str
    max_power: str
    torque: str
    seats: int

class CarCreate(CarBase):
    pass

class CarResponse(CarBase):
    id: int

    class Config:
        orm_mode = True
