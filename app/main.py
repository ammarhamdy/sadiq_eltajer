import logging
import sys
import asyncio

from reporter.summry_repoter import summarise_response, print_summary
from app.services.data_service import fetch_ad_titles
from app.services.http_service import send_request
from app.services.request_builder import RequestBuilder


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("logs/sadiq-eltajer-1.log", encoding="utf-8", mode="w")
    ],
)

log = logging.getLogger(__name__)


async def main() -> None:
    cookies = "XSRF-TOKEN=eyJpdiI6Ik81QW5xOVBRZUFwVkdJTEt3MFd6RFE9PSIsInZhbHVlIjoiUlpzZmtzUFp3ZXREZmlWYy9MSHoxbG5ReXg3S0V0U1g3bU5GSFZyZkV6YkVKZlJETk1IMUdjK3RaRENGUVEybHdpdEhRS2MzcmsxdTBjU2xrVG9scVNYdkhBdlNEL2lvb3dmTElDVHBJaE5VMTkwaTVxN01DZHlxTHBPUEVmOEIiLCJtYWMiOiJiNjI3YmZmODc5NTFhNjdiMjQzYjJmMjY3MmU3YWVkNzQzNGEwYTgyNzdiZGM3NTQyYmU0NGRiYmE2MjkxMWVhIiwidGFnIjoiIn0%3D; aqarat_session=eyJpdiI6IjQrUWlKL3RnZkJFYzIycGFTYUNyZXc9PSIsInZhbHVlIjoiMXlFZjRRd3huZ0tRMk1BN2lnZTFyZzdMQTFvT0U4QTFWL0s3NVNYMmZ1TmFrWllvUnVPMU9kTU5TaHFoTXBMbzRPa0UwUDErODRsWXVRNmlOS2VxUmlmNE10TDNDRU1XcjVoQjlZQVRwSXJTWkhMTFh1TURrbFhvMmZickFVVjYiLCJtYWMiOiIxMDI4MzZhYmI3YzZmZDk4NDFjMmU1ZWEyZjBiYTFkYTExMjNlMzE5OWQ3MjQ3YjBhZTQyODAzMzgxNmFjMGVlIiwidGFnIjoiIn0%3D"
    api_token = "o3fNzP7ZeAX97q5mjjtqRVon51jrOol8"
    titles = await asyncio.to_thread(fetch_ad_titles)

    semaphore = asyncio.Semaphore(1)

    async def process_title(title: str):
        async with semaphore:
            request = (
                RequestBuilder()
                .set_prompt(title)
                .set_auth(cookie=cookies, api_token=api_token)
                .build()
            )
            return await send_request(
                request=request,
                max_retries=3,
                retry_delay=1,
            )

    tasks = [asyncio.create_task(process_title(title)) for title in titles]

    for task in asyncio.as_completed(tasks):
        try:
            result = await task
            print_summary(summarise_response(result))
            # print_response(result)
        except Exception:
            log.exception("Request failed")


if __name__ == "__main__":
    asyncio.run(main())