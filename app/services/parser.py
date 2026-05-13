"""HTML response parsing utilities."""

from __future__ import annotations
import httpx
from bs4 import BeautifulSoup


class ResponseParser:
    """Stateless utility for extracting data from HTTP responses."""

    TOKEN_FIELD = "token"

    @staticmethod
    def extract_csrf_token(response: httpx.Response) -> str | None:
        """
        Extract the CSRF token from a login page HTML response.

        Args:
            response: The raw HTTP response from the login page.

        Returns:
            The token string if found, otherwise None.
        """
        soup = BeautifulSoup(response.text, "html.parser")
        token_input = soup.find("input", attrs={"name": ResponseParser.TOKEN_FIELD})
        if not token_input:
            return None
        return token_input.get("value") or None