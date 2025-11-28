# src/utils/retry.py
import time
import random
from functools import wraps
from typing import Callable, Type, TypeVar, ParamSpec, Concatenate
from loguru import logger
from src.core.utils.exceptions import RetryableError, ZerodhaAPIError

P = ParamSpec("P")
R = TypeVar("R")

def retry(
    max_attempts: int = 5,
    delay: float = 1.0,
    backoff: float = 2.0,
    jitter: bool = True,
    retry_on: tuple[Type[Exception], ...] = (RetryableError, ZerodhaAPIError),
):
    def decorator(fn: Callable[Concatenate[..., P], R]) -> Callable[..., R]:
        @wraps(fn)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            attempt = 0
            current_delay = delay

            while attempt < max_attempts:
                try:
                    return fn(*args, **kwargs)
                except retry_on as exc:
                    attempt += 1
                    if attempt >= max_attempts:
                        logger.error(f"Failed after {max_attempts} attempts: {exc}")
                        raise

                    sleep_time = current_delay + (random.uniform(0, 1) if jitter else 0)
                    logger.warning(f"Attempt {attempt} failed: {exc}. Retrying in {sleep_time:.2f}s...")
                    time.sleep(sleep_time)
                    current_delay *= backoff
                except Exception as exc:
                    logger.error(f"Non-retryable error in {fn.__name__}: {exc}")
                    raise
            return None  # unreachable
        return wrapper
    return decorator