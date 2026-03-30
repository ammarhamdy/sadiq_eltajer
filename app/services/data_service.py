from app.db import get_connection
from app.queries import GET_ADS


def fetch_ads():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(GET_ADS)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


if __name__ == '__main__':
    from pprint import pprint

    for ad in fetch_ads():
        pprint(ad)

