import logging
from typing import  Optional
import httpx
from httpx import AsyncClient, Response
from core.config import BASE_URL
from core.decorations import timeout_guard
from services.header_generator import  default_headers
from services.parser import ResponseParser


logger = logging.getLogger(__name__)
CHAT_URL = BASE_URL + "/chat"
KEYWORDS_LIST_URL = BASE_URL + "/api/ads/keywords-list"
ASK_URL = BASE_URL + "/api/ads/keywords-list"
RETRY_DELAYS: tuple[float, ...] = (
    0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 3.0, 5.0, 7.5, 10.0
)


class HTTPService:

    def __init__(self, timeout: float = 30.0) -> None:
        self._client: Optional[AsyncClient] = None
        self._token: str | None = None
        self._timeout = timeout

    async def __aenter__(self) -> "HTTPService":
        self._client = AsyncClient(timeout=self._timeout)
        return self

    async def __aexit__(self, *_: object) -> None:
        if self._client:
            await self._client.aclose()
            self._client = None

    async def run(self, keyword: str, page: int=1) -> Response | None:
        assert self._client is not None, "Use HTTPService as an async context manager."
        logger.info("Initializing session…")
        if not await self._acquire_token():
            logger.error("Failed to retrieve CSRF token. Aborting.")
            return None
        response = await self._get_keywords_list(keyword=keyword, page=page)
        if not response:
            logger.error(f"No Response for _get_keywords_list({keyword}). Aborting.")
            return None
        return response

    async def _acquire_token(self) -> bool:
        """
        Fetch the login page and extract the CSRF token.

        Returns:
            True if the token was successfully obtained, False otherwise.
        """
        try:
            if self._client is None:
                return False
            response = await self._client.get(BASE_URL)
            self._token = ResponseParser.extract_csrf_token(response)
            return self._token is not None
        except httpx.HTTPError as exc:
            logger.error("HTTP error during token acquisition: %s", exc)
            return False
        except Exception as exc:  # noqa: BLE001
            logger.error("Unexpected error during token acquisition: %s", exc)
            return False

    @timeout_guard()
    async def _get_keywords_list(self, keyword: str, page: int = 1) -> Response | None:
        if not self._client:
            return None
        return await self._client.get(
            KEYWORDS_LIST_URL,
            headers=default_headers(),
            cookies=self._client.cookies,
            params={
                "keyword": keyword,
                "per_page": 100,
                "page": page,
            },
        )

