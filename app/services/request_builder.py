"""
request_builder.py
~~~~~~~~~~~~~~~~~~
A clean, reusable request-builder for the Sadiq El-Tajer smart-assistant API.
"""

from __future__ import annotations
import json
import logging
import copy
from typing import Any, Optional
import httpx
from config import BASE_URL
from app.services.search_payload import SearchPayload, _DEFAULT_HEADERS

logger = logging.getLogger(__name__)

# RequestBuilder
class RequestBuilder:
    """
    Fluent builder for the smart-assistant GET request.

    Usage
    -----
    >>> req = (
    ...     RequestBuilder()
    ...     .set_prompt("فيلا للبيع في حي الروابي")
    ...     .set_max_tokens(1700)
    ...     .set_auth(cookie="...", api_token="...")
    ...     .set_payload(SearchPayload(city="بريدة", type="فلة"))
    ...     .build()
    ... )
    >>> response = httpx.get(**req)
    """

    DEFAULT_TIMEOUT = 30  # seconds
    DEFAULT_MAX_TOKENS = 1700

    def __init__(self) -> None:
        self._prompt: str = ""
        self._max_tokens: int = self.DEFAULT_MAX_TOKENS
        self._payload: SearchPayload = SearchPayload()
        self._headers: dict[str, str] = copy.deepcopy(_DEFAULT_HEADERS)
        self._timeout: int = self.DEFAULT_TIMEOUT
        self._extra_params: dict[str, Any] = {}

    def set_prompt(self, prompt: str) -> "RequestBuilder":
        """Set the natural-language search prompt (Arabic supported)."""
        if not prompt or not prompt.strip():
            raise ValueError("prompt must be a non-empty string")
        self._prompt = prompt.strip()
        return self

    def set_max_tokens(self, max_tokens: int) -> "RequestBuilder":
        """Override the default max_completion_tokens (default: 1700)."""
        if max_tokens <= 0:
            raise ValueError("max_tokens must be a positive integer")
        self._max_tokens = max_tokens
        return self

    def set_payload(self, payload: SearchPayload) -> "RequestBuilder":
        """Attach a fully-configured SearchPayload instance."""
        if not isinstance(payload, SearchPayload):
            raise TypeError(f"expected SearchPayload, got {type(payload).__name__}")
        self._payload = payload
        return self

    def set_auth(self, *, cookie: str, api_token: str) -> "RequestBuilder":
        """
        Inject sensitive credentials.
        Kept separate so the rest of the builder stays credential-free.
        """
        if not cookie or not api_token:
            raise ValueError("both cookie and api_token are required")
        self._headers["cookie"] = cookie
        self._headers["x-app-api-token"] = api_token
        return self

    def set_timeout(self, seconds: int) -> "RequestBuilder":
        """Override the default request timeout (default: 30 s)."""
        if seconds <= 0:
            raise ValueError("timeout must be positive")
        self._timeout = seconds
        return self

    def add_header(self, key: str, value: str) -> "RequestBuilder":
        """Add or override a single request header."""
        self._headers[key.lower()] = value
        return self

    def add_param(self, key: str, value: Any) -> "RequestBuilder":
        """Inject an extra query-parameter not covered by the standard API."""
        self._extra_params[key] = value
        return self

    def build(self) -> dict[str, Any]:
        """
        Validate state, assemble and log the request dict.

        Returns
        -------
        dict  — keyword-arguments ready for ``httpx.get(**result)``.

        Raises
        ------
        ValueError  if required fields (prompt, credentials) are missing.
        """
        self._validate()

        params: dict[str, Any] = {
            "keyword": self._prompt,
            "per_page": "1000",
            "page": "1",
            "max_completion_tokens": str(self._max_tokens),
            "current_search_payload": self._payload.to_json(),
            **self._extra_params,
        }

        request: dict[str, Any] = {
            "url": BASE_URL,
            "params": params,
            "headers": self._headers,
            "timeout": self._timeout,
        }

        self._log_request(request)
        return request

    #  Private helpers
    def _validate(self) -> None:
        errors: list[str] = []
        if not self._prompt:
            errors.append("prompt is required — call .set_prompt()")
        if "cookie" not in self._headers:
            errors.append("cookie is required — call .set_auth()")
        if "x-app-api-token" not in self._headers:
            errors.append("api_token is required — call .set_auth()")
        if errors:
            raise ValueError("RequestBuilder.build() failed:\n  " + "\n  ".join(errors))

    def _log_request(self, request: dict[str, Any]) -> None:
        """Log request details with sensitive header values masked."""
        # safe_headers = {
        #     k: ("***MASKED***" if k.lower() in _SENSITIVE_HEADERS else v)
        #     for k, v in request["headers"].items()
        # }
        logger.info("Request URL    : %s", request["url"][:100] + '..')
        logger.info(
            "Query params   :\n%s",
            json.dumps(request["params"], ensure_ascii=False, indent=2)[:100] + '..',
        )
        # logger.info(
        #     "Request headers:\n%s",
        #     json.dumps(safe_headers, indent=2),
        # )

    #  Convenience: re-usable factory presets
    @classmethod
    def for_land_search(
            cls,
            prompt: str,
            *,
            city: Optional[str] = None,
            neighborhood: Optional[str] = None,
            plot_number: Optional[str] = None,
    ) -> "RequestBuilder":
        """Preset for land (ارض) searches — common in this dataset."""
        payload = SearchPayload(
            city=city,
            neighborhood=neighborhood,
            plot_number=plot_number,
            classification="سكني",
            type="ارض",
        )
        return cls().set_prompt(prompt).set_payload(payload)

    @classmethod
    def for_villa_search(
            cls,
            prompt: str,
            *,
            city: Optional[str] = None,
            neighborhood: Optional[str] = None,
            min_price: Optional[float] = None,
            max_price: Optional[float] = None,
    ) -> "RequestBuilder":
        """Preset for villa (فلة / فله) searches."""
        payload = SearchPayload(
            city=city,
            neighborhood=neighborhood,
            min_price=min_price,
            max_price=max_price,
            type="فلة",
        )
        return cls().set_prompt(prompt).set_payload(payload)


if __name__ == '__main__':
    COOKIE = "timezone=Asia/Beirut; aqarat_session=abc123; ..."
    API_TOKEN = "o3fNzP7ZeAX97q5mjjtqRVon51jrOol8"

    # ── 1. Full fluent chain ───────────────────────────────────────────────────
    req = (
        RequestBuilder()
        .set_prompt("دبلكس للبيع في حي الروابي بريدة يقبل البنك")
        .set_max_tokens(1700)
        .set_auth(cookie=COOKIE, api_token=API_TOKEN)
        .set_payload(
            SearchPayload(
                city="بريدة",
                neighborhood="الروابي",
                type="دبلكس",
                max_price=900_000,
            )
        )
        .build()
    )
    response = httpx.get(**req)

    # ── 2. Preset factory — land search ───────────────────────────────────────
    req = (
        RequestBuilder
        .for_land_search(
            "ارض في مخطط الجامعة حي الغدير بريدة",
            city="بريدة",
            neighborhood="الغدير",
            plot_number="7080",
        )
        .set_auth(cookie=COOKIE, api_token=API_TOKEN)
        .build()
    )
    response = httpx.get(**req)

    # ── 3. Preset factory — villa search ──────────────────────────────────────
    req = (
        RequestBuilder
        .for_villa_search(
            "فله مودرن للبيع في حي الشفاء بريدة تقبل البنك",
            city="بريدة",
            neighborhood="الشفاء",
            max_price=1_500_000,
        )
        .set_auth(cookie=COOKIE, api_token=API_TOKEN)
        .build()
    )
    response = httpx.get(**req)
