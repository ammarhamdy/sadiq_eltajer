import asyncio

from services.http_service import HTTPService


async def random_ask():
    async with HTTPService() as client:
        return await client.run("القصيم", 1)


if __name__ == "__main__":
    try:
        asyncio.run(random_ask())
    except KeyboardInterrupt:
        print("Ctrl+C")