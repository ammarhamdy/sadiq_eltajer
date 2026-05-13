from dataclasses import dataclass
from model.BaseEntity import BaseEntity


@dataclass(slots=True, frozen=True)
class Cities(BaseEntity):
    pass