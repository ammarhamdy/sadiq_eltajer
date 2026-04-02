from core.db import get_connection
from queries.property_queries import GET_ADS, GET_ALIVE_ADS


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


def fetch_alive_ads():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(GET_ALIVE_ADS)
            return [row[0] for row in cursor.fetchall()]


if __name__ == '__main__':
    from pprint import pprint

    for ad in fetch_alive_ads():
        pprint(ad)


