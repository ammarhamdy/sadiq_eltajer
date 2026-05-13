from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class BaseEntity:
    id: int
    name: str


