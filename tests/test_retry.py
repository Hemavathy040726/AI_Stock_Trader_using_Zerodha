# tests/test_retry.py
from src.core.utils.retry import retry


def test_retry_success_after_failures():
    calls = 0

    @retry(max_attempts=3, delay=0.01, retry_on=(ValueError,))  # ← ADD THIS!
    def flaky():
        nonlocal calls
        calls += 1
        if calls < 3:
            raise ValueError("temp fail")
        return "success"

    result = flaky()
    assert result == "success"
    assert calls == 3  # proves it retried twice