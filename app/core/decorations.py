import logging
import httpx
from functools import wraps


logger = logging.getLogger(__name__)


def timeout_guard():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except httpx.TimeoutException as exc:
                logger.error("Request timed out (attempt %d): %s", exc)
                return None
            except httpx.RequestError as exc:
                logger.error("Request error (attempt %d): %s", exc)
                return None
        return wrapper
    return decorator