import asyncio
import json
import logging
from typing import Any, Optional
import httpx


logger = logging.getLogger(__name__)


async def send_request(
    request: dict[str, Any],
    max_retries: int,
    retry_delay: float,
) -> httpx.Response:
    """
    Execute the GET request with retry logic.
    Raises the last exception if all attempts fail.
    """
    last_exception: Optional[Exception] = None

    async with httpx.AsyncClient() as client:
        for attempt in range(1, max_retries + 1):
            try:
                logger.info("Attempt %d / %d …", attempt, max_retries)

                response = await client.get(**request)

                if response.status_code != 200:
                    logger.warning(
                        "Non-200 response: HTTP %d — %s",
                        response.status_code,
                        response.text[:300],
                    )
                    last_exception = httpx.HTTPStatusError(
                        f"HTTP {response.status_code}",
                        request=response.request,
                        response=response,
                    )
                else:
                    logger.info("HTTP %d — success.", response.status_code)
                    return response

            except httpx.TimeoutException as exc:
                logger.error("Request timed out (attempt %d): %s", attempt, exc)
                last_exception = exc

            except httpx.RequestError as exc:
                logger.error("Request error (attempt %d): %s", attempt, exc)
                last_exception = exc

            if attempt < max_retries:
                logger.info("Retrying in %s s …", retry_delay)
                await asyncio.sleep(retry_delay)

    if last_exception is not None:
        raise last_exception
    raise RuntimeError("Request failed without an explicit exception")


def print_response(response: httpx.Response) -> None:
    """Pretty-print JSON body; fall back to raw text on decode failure."""
    # logger.info("Response headers: %s", dict(response.headers))

    try:
        payload = response.json()
        print("\n─── Response JSON ───────────────────────────────────────────")
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        print("─────────────────────────────────────────────────────────────\n")
    except json.JSONDecodeError:
        logger.warning("Response is not valid JSON — printing raw text instead.")
        print("\n─── Response Text ───────────────────────────────────────────")
        print(response.text)
        print("─────────────────────────────────────────────────────────────\n")


