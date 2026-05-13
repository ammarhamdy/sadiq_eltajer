from typing import Iterable, Type

from model.Ad import Ad
from model.BaseEntity import BaseEntity


def map_alive_entities[T: BaseEntity](
    rows: Iterable[tuple[int, str]],
    model: Type[T],
) -> list[T]:
    return [
        model(id=id_, name=name)
        for id_, name in rows
    ]


from collections.abc import Iterable


def map_ads(rows: Iterable[tuple]) -> list[Ad]:
    return [
        Ad(
            title=title,
            classifications=classifications,
            types=types,
            price=price,
            price_type=price_type,
            area_id=area_id,
            city_id=city_id,
            neighborhood_id=neighborhood_id,
            number_of_rooms=number_of_rooms,
            number_of_bathrooms=number_of_bathrooms,
            area_by_meter=area_by_meter,
            street_frontage=street_frontage,
        )
        for (
            title,
            classifications,
            types,
            price,
            price_type,
            area_id,
            city_id,
            neighborhood_id,
            number_of_rooms,
            number_of_bathrooms,
            area_by_meter,
            street_frontage,
        ) in rows
    ]