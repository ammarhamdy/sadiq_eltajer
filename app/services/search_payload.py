import json
from dataclasses import dataclass, field
from typing import Optional


# Immutable default headers — never mutated at runtime
_DEFAULT_HEADERS: dict[str, str] = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9,ar;q=0.8",
    "priority": "u=1, i",
    "referer": "https://sadiq-eltajer.sa/",
    "sec-ch-ua": '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
    ),
}


# Header keys whose runtime values must never appear in plain-text logs
_SENSITIVE_HEADERS: frozenset[str] = frozenset({
    "cookie",
    "x-app-api-token",
    "authorization",
})


# Search payload dataclass
@dataclass
class SearchPayload:
    """
    Mirrors the `current_search_payload` JSON structure expected by the API.
    All fields are optional; None serialises as JSON null.
    """
    intent: str = "search_ads"
    target_object: str = "unknown"
    strategy: str = "keywords_first"
    area: Optional[str] = None
    city: Optional[str] = None
    neighborhood: Optional[str] = None
    classification: Optional[str] = None
    type: Optional[str] = None
    classification_type: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    rooms: Optional[int] = None
    baths: Optional[int] = None
    min_area: Optional[float] = None
    max_area: Optional[float] = None
    plot_number: Optional[str] = None
    plate_number: Optional[str] = None
    land_number: Optional[str] = None
    exclude_negotiable: Optional[bool] = None
    only_negotiable: Optional[bool] = None
    sort_by: Optional[str] = None
    sort_order: Optional[str] = None
    top_result_mode: Optional[str] = None

    def to_json(self) -> str:
        """Serialise to the JSON string the API expects as a query-param value."""
        return json.dumps(self.__dict__, ensure_ascii=False)

