from dataclasses import dataclass
from model.BaseEntity import BaseEntity


@dataclass(slots=True, frozen=True)
class Neighborhoods(BaseEntity):
    pass