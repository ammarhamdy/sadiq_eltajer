import json
from dataclasses import dataclass, field
from typing import Optional


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

