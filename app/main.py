import logging
import sys
import asyncio
from app.services.data_service import fetch_ads
from app.services.http_service import send_user


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("sadiq-eltajer.log", encoding="utf-8"),
    ],
)


log = logging.getLogger(__name__)




async def main():
    users = fetch_ads()

    tasks = [send_user(user) for user in users]

    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())