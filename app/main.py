import logging
import sys
import asyncio
from app.services.data_service import fetch_ad_titles
from app.services.http_service import send_request
from app.services.request_builder import RequestBuilder


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
    cookies = "XSRF-TOKEN=eyJpdiI6Ik81QW5xOVBRZUFwVkdJTEt3MFd6RFE9PSIsInZhbHVlIjoiUlpzZmtzUFp3ZXREZmlWYy9MSHoxbG5ReXg3S0V0U1g3bU5GSFZyZkV6YkVKZlJETk1IMUdjK3RaRENGUVEybHdpdEhRS2MzcmsxdTBjU2xrVG9scVNYdkhBdlNEL2lvb3dmTElDVHBJaE5VMTkwaTVxN01DZHlxTHBPUEVmOEIiLCJtYWMiOiJiNjI3YmZmODc5NTFhNjdiMjQzYjJmMjY3MmU3YWVkNzQzNGEwYTgyNzdiZGM3NTQyYmU0NGRiYmE2MjkxMWVhIiwidGFnIjoiIn0%3D; aqarat_session=eyJpdiI6IjQrUWlKL3RnZkJFYzIycGFTYUNyZXc9PSIsInZhbHVlIjoiMXlFZjRRd3huZ0tRMk1BN2lnZTFyZzdMQTFvT0U4QTFWL0s3NVNYMmZ1TmFrWllvUnVPMU9kTU5TaHFoTXBMbzRPa0UwUDErODRsWXVRNmlOS2VxUmlmNE10TDNDRU1XcjVoQjlZQVRwSXJTWkhMTFh1TURrbFhvMmZickFVVjYiLCJtYWMiOiIxMDI4MzZhYmI3YzZmZDk4NDFjMmU1ZWEyZjBiYTFkYTExMjNlMzE5OWQ3MjQ3YjBhZTQyODAzMzgxNmFjMGVlIiwidGFnIjoiIn0%3D"
    api_token = "o3fNzP7ZeAX97q5mjjtqRVon51jrOol8"
    titles = fetch_ad_titles()
    tasks = [
        send_request(
            request=RequestBuilder().set_prompt(
                prompt=title
            ).set_auth(
                cookie=cookies,
                api_token=api_token,
            ).build(),
            max_retries=3,
            retry_delay=1,
        ) for title in titles
    ][0:1]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    ##
    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())