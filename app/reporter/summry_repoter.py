"""
response_summary.py
~~~~~~~~~~~~~~~~~~~
Summarise a paginated listing API response into a compact,
human-readable digest — frequencies, distributions, and key stats.
"""

from __future__ import annotations
import json
from collections import Counter
from dataclasses import dataclass, field
from typing import Any

import httpx
from httpx import Response


# ---------------------------------------------------------------------------
# Typed summary result — no raw dicts escaping this module
# ---------------------------------------------------------------------------

@dataclass
class ListingSummary:
    total_results: int
    pages: int
    per_page: int

    # frequency distributions
    by_classification: dict[str, int] = field(default_factory=dict)
    by_type: dict[str, int] = field(default_factory=dict)
    by_neighborhood: dict[str, int] = field(default_factory=dict)
    by_city: dict[str, int] = field(default_factory=dict)
    by_area: dict[str, int] = field(default_factory=dict)
    by_price_type: dict[str, int] = field(default_factory=dict)
    by_status: dict[str, int] = field(default_factory=dict)

    # price stats (priced listings only — zeros excluded)
    priced_count: int = 0
    non_priced_count: int = 0
    min_price: float = 0.0
    max_price: float = 0.0
    avg_price: float = 0.0

    # area stats (m²)
    min_area_m2: float = 0.0
    max_area_m2: float = 0.0
    avg_area_m2: float = 0.0

    # flags
    featured_count: int = 0
    with_images: int = 0  # has a real (non-default) main image


# Core formatter
def summarise_response(response: httpx.Response) -> ListingSummary:
    """
    Parse the API envelope and return a :class:`ListingSummary`.

    Parameters
    ----------
    response:
        httpx response object containing the API response.

    Raises
    ------
    KeyError / ValueError  if the envelope shape is unexpected.
    """
    # The full parsed JSON dict as returned by the API.
    raw = _convert_response(response)

    data_block = raw["data"]
    meta = data_block["meta"]
    listings: list[dict] = data_block["data"]

    if not listings:
        return ListingSummary(
            total_results=meta.get("total", 0),
            pages=meta.get("last_page", 0),
            per_page=meta.get("per_page", 0),
        )

    # ── Frequency counters ─────────────────────────────────────────────────
    c_classification = Counter[str]()
    c_type = Counter[str]()
    c_neighborhood = Counter[str]()
    c_city = Counter[str]()
    c_area = Counter[str]()
    c_price_type = Counter[str]()
    c_status = Counter[str]()

    # ── Numeric accumulators ───────────────────────────────────────────────
    prices: list[float] = []
    areas_m2: list[float] = []
    unpriced = 0
    featured = 0
    with_images = 0

    DEFAULT_IMG = "https://sadiq-eltajer.sa/default.jpg"

    for ad in listings:
        # -- counters
        c_classification[ad.get("classification", "—")] += 1
        c_type[ad.get("type", "—")] += 1
        c_neighborhood[ad.get("neighborhood", "—")] += 1
        c_city[ad.get("city", "—")] += 1
        c_area[ad.get("area", "—")] += 1
        c_price_type[ad.get("price_type", "—")] += 1
        c_status[ad.get("status", "—")] += 1

        # -- price
        price = ad.get("price") or 0
        if price and price > 0:
            prices.append(float(price))
        else:
            unpriced += 1

        # -- area m²
        area_m2 = ad.get("area_by_meter") or 0
        if area_m2 and area_m2 > 0:
            areas_m2.append(float(area_m2))

        # -- flags
        if ad.get("is_featured"):
            featured += 1
        if ad.get("main_image") and ad["main_image"] != DEFAULT_IMG:
            with_images += 1

    return ListingSummary(
        total_results=meta["total"],
        pages=meta["last_page"],
        per_page=meta["per_page"],
        by_classification=dict(c_classification.most_common()),
        by_type=dict(c_type.most_common()),
        by_neighborhood=dict(c_neighborhood.most_common()),
        by_city=dict(c_city.most_common()),
        by_area=dict(c_area.most_common()),
        by_price_type=dict(c_price_type.most_common()),
        by_status=dict(c_status.most_common()),
        priced_count=len(prices),
        non_priced_count=unpriced,
        min_price=min(prices, default=0.0),
        max_price=max(prices, default=0.0),
        avg_price=sum(prices) / len(prices) if prices else 0.0,
        min_area_m2=min(areas_m2, default=0.0),
        max_area_m2=max(areas_m2, default=0.0),
        avg_area_m2=sum(areas_m2) / len(areas_m2) if areas_m2 else 0.0,
        featured_count=featured,
        with_images=with_images,
    )

def _convert_response(response: httpx.Response) -> dict[str, Any]:
    return response.json()


def _bar(value: int, total: int, width: int = 20) -> str:
    """Inline ASCII progress bar."""
    filled = round(value / total * width) if total else 0
    return f"[{'█' * filled}{'░' * (width - filled)}]"


def print_summary(s: ListingSummary) -> None:
    """Render a :class:`ListingSummary` as a human-readable report."""

    sep = "─" * 52
    sep2 = "━" * 52

    def _freq_table(label: str, counter: dict[str, int]) -> None:
        total = sum(counter.values())
        print(f"\n  {label}")
        # print(f"  {'Value':<28} {'Count':>5}  {'%':>5}  Bar")
        print(f"  {'─' * 28} {'─' * 5}  {'─' * 5}  {'─' * 20}")
        for k, v in counter.items():
            pct = v / total * 100 if total else 0
            bar = _bar(v, total)
            print(f"  {k:<28} {v:>5}  {pct:>4.0f}%  {bar}")

    print(f"\n{sep2}")
    print(f"  LISTING RESPONSE SUMMARY")
    print(f"{sep2}")
    print(f"  Total results : {s.total_results:,}")
    print(f"  Pages         : {s.pages}  (page size: {s.per_page})")
    print(f"  In this page  : {s.priced_count + s.non_priced_count}")
    print(sep)

    # ── Frequency distributions ────────────────────────────────────────────
    _freq_table("Classification", s.by_classification)
    _freq_table("Property Type", s.by_type)
    _freq_table("Neighborhood", s.by_neighborhood)
    _freq_table("City", s.by_city)
    _freq_table("Area/Region", s.by_area)
    _freq_table("Price Type", s.by_price_type)
    _freq_table("Status", s.by_status)

    # ── Price stats ────────────────────────────────────────────────────────
    print(f"\n{sep}")
    print(f"  PRICE STATS  (zeros / 'ignore_negotiable' excluded)")
    print(f"  {'Priced listings':<28} {s.priced_count:>5}")
    print(f"  {'Unpriced / undisclosed':<28} {s.non_priced_count:>5}")
    if s.priced_count:
        print(f"  {'Min price (SAR)':<28} {s.min_price:>12,.0f}")
        print(f"  {'Max price (SAR)':<28} {s.max_price:>12,.0f}")
        print(f"  {'Avg price (SAR)':<28} {s.avg_price:>12,.0f}")

    # ── Area stats ─────────────────────────────────────────────────────────
    print(f"\n{sep}")
    print(f"  AREA STATS (m²)")
    print(f"  {'Min':<28} {s.min_area_m2:>8,.0f} m²")
    print(f"  {'Max':<28} {s.max_area_m2:>8,.0f} m²")
    print(f"  {'Avg':<28} {s.avg_area_m2:>8,.0f} m²")

    # ── Flags ──────────────────────────────────────────────────────────────
    print(f"\n{sep}")
    print(f"  FLAGS")
    print(f"  {'Featured':<28} {s.featured_count:>5}")
    print(f"  {'Has real image':<28} {s.with_images:>5}")
    print(f"{sep2}\n")


if __name__ == "__main__":
    import sys

    # accept JSON from a file path arg or stdin
    source = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    with source as fh:
        raw = json.load(fh)

    summary = summarise_response(raw)
    print_summary(summary)
