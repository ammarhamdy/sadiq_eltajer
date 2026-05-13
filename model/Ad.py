from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass(slots=True, frozen=True)
class Ad:
    title: str
    classifications: str
    types: str

    price: Decimal
    price_type: str

    area_id: int
    city_id: int
    neighborhood_id: int

    number_of_rooms: Optional[int]
    number_of_bathrooms: Optional[int]

    area_by_meter: Optional[float]
    street_frontage: Optional[float]