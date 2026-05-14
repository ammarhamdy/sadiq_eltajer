from core.db import get_connection
from model.Areas import Areas
from model.Types import Types
from model.Neighborhoods import Neighborhoods
from model.Cities import Cities
from model.Classifications import Classifications
from queries.mapper import *
from queries.queries import *


def fetch_ads():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(GET_ADS)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def fetch_ad_titles():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(GET_ADS)
            return


def fetch_alive_ads() -> list[Ad]:
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(GET_ALIVE_ADS)
            rows = cursor.fetchall()
            return map_ads(rows)


def fetch_alive_entities[T: BaseEntity](
    query: str,
    model: Type[T],
) -> list[T]:
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            rows: list[tuple[int, str]] = cursor.fetchall()
            return map_alive_entities(rows, model)


def fetch_alive_areas():
    return fetch_alive_entities(GET_ALIVE_AREAS, Areas)


def fetch_alive_cities():
    return fetch_alive_entities(GET_ALIVE_CITIES, Cities)


def fetch_alive_neighborhoods():
    return fetch_alive_entities(GET_ALIVE_NEIGHBORHOODS, Neighborhoods)


def fetch_alive_types():
    return fetch_alive_entities(GET_ALIVE_TYPES, Types)


def fetch_alive_classifications():
    return fetch_alive_entities(GET_ALIVE_CLASSIFICATIONS, Classifications)


if __name__ == '__main__':
    from pprint import pprint

    for i, item in enumerate(fetch_alive_areas()):
        pprint(item)

    print("\n")
    for i, item in enumerate(fetch_alive_cities()):
        pprint(item)

    print("\n")
    for i, item in enumerate(fetch_alive_neighborhoods()):
        pprint(item)

    print("\n")
    for i, item in enumerate(fetch_alive_types()):
        pprint(item)

    print("\n")
    for i, item in enumerate(fetch_alive_classifications()):
        pprint(item)

    print("\n")
    for i, item in enumerate(fetch_alive_ads()):
        pprint(item)

