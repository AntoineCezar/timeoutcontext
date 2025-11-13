from __future__ import annotations

import signal
from contextlib import ContextDecorator
from types import FrameType, TracebackType
from typing import Any


def raise_timeout(signum: int, frame: FrameType | None) -> Any:
    raise TimeoutError()


class timeout(ContextDecorator):
    """Raises TimeoutError when the gien time in seconds elapsed.

    As a context manager:

        >>> import sys
        >>> from time import sleep
        >>> from timeoutcontext import timeout
        >>>
        >>> try:
        ...     with timeout(1):
        ...         sleep(2)
        ... except TimeoutError:
        ...     print('timeout')
        ...
        timeout

    As a decorator:

        >>> import sys
        >>> from time import sleep
        >>> from timeoutcontext import timeout
        >>>
        >>> @timeout(1)
        ... def wait():
        ...     sleep(2)
        ...
        >>> try:
        ...     wait()
        ... except TimeoutError:
        ...     print('timeout')
        ...
        timeout
    """

    def __init__(self, seconds: float | None) -> None:
        self._seconds = seconds

    def __enter__(self) -> timeout:
        if self._seconds:
            self._replace_alarm_handler()
            signal.setitimer(signal.ITIMER_REAL, self._seconds)
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        if self._seconds:
            self._restore_alarm_handler()
            signal.alarm(0)

    def _replace_alarm_handler(self) -> None:
        self._old_alarm_handler = signal.signal(signal.SIGALRM, raise_timeout)

    def _restore_alarm_handler(self) -> None:
        signal.signal(signal.SIGALRM, self._old_alarm_handler)
