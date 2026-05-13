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


"""
curl --path-as-is -i -s -k -X $'GET' \
    -H $'Host: sadiq-eltajer.sa' -H $'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:150.0) Gecko/20100101 Firefox/150.0' -H $'Accept: application/json' -H $'Accept-Language: en-US,en;q=0.9' -H $'Accept-Encoding: gzip, deflate, br' -H $'Referer: https://sadiq-eltajer.sa/' -H $'X-App-Api-Token: o3fNzP7ZeAX97q5mjjtqRVon51jrOol8' -H $'Sec-Fetch-Dest: empty' -H $'Sec-Fetch-Mode: cors' -H $'Sec-Fetch-Site: same-origin' -H $'Priority: u=4' -H $'Te: trailers' \
    -b $'XSRF-TOKEN=eyJpdiI6IjlqcDNqQ2ZSNHZEeStOSVBnQ0VRSmc9PSIsInZhbHVlIjoiWVJCb2hlWmxyNXpxU08rbEZwOXNxSmdCTE5DRDduTGEwaFB0QlpSQ1BrNXY2cVR5QzFRcVp1SFlZaFY4dVY2WlZvY0tPMjMzbG5UcStqcTJmUDdQZFcrRWJNUHk0em9Jcy94bkVsbUFMdFRNZytCdmlieExmbEdZZmwxTHl3Tk8iLCJtYWMiOiI3MDg3M2Q0NjMyZTJmZjE3ZjNlZGVhYjY1OGY5M2YxNDlkZmMyMDFhMzZmYTVmMGEzOWExMTlmYzVhYTI3YzI4IiwidGFnIjoiIn0%3D; aqarat_session=eyJpdiI6IkYwSjNmZUxGWEZEWHBzdHl3cGo4VkE9PSIsInZhbHVlIjoiMW1WUFAzS2lldFE0YUREaHBBUTJiM0R1aHREZjBTdzZBVGJFOVhRajZpMVlSd29ZMFBKWlJTTkRhcTRHSElQM2V6NFlIcnZUOG1vV3pUYmxPaHFsbFR1K0w0SlhlQ1FMbHdkb1lSM2RRdjJHOHJGYUR0N1pnVzhrUFg2UXRRc3ciLCJtYWMiOiI3MDYwNjRlY2I1MDc0NDFkOWVhMzNhMDIwYTdjZjI4NjI3MDZiYTlkNDQ4YzUzZjViYjQ4MjQ1OTk2NTdmM2MzIiwidGFnIjoiIn0%3D' \
    $'https://sadiq-eltajer.sa/api/ads/keywords-list?keyword=%D8%A7%D9%84%D9%82%D8%B5%D9%8A%D9%85&per_page=100&page=1'
"""