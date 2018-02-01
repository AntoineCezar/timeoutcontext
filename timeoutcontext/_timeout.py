# -*- coding: utf-8 -*-

import sys
import signal
if sys.version_info < (3, 2):
    from contextdecorator import ContextDecorator
else:
    from contextlib import ContextDecorator


if sys.version_info < (3, 3):
    class TimeoutError(Exception):
        pass


def raise_timeout(signum, frame):
    raise TimeoutError()


class timeout(ContextDecorator):
    """Raises TimeoutError when the gien time in seconds elapsed.

        As a context manager:

            >>> import sys
            >>> from time import sleep
            >>> from timeoutcontext import timeout
            >>> if sys.version_info < (3, 3):
            ...     from timeoutcontext import TimeoutError
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
            >>> if sys.version_info < (3, 3):
            ...     from timeoutcontext import TimeoutError
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

    def __init__(self, seconds):
        self._seconds = seconds

    def __enter__(self):
        if self._seconds:
            self._replace_alarm_handler()
            signal.setitimer(signal.ITIMER_REAL, self._seconds)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._seconds:
            self._restore_alarm_handler()
            signal.alarm(0)

    def _replace_alarm_handler(self):
        self._old_alarm_handler = signal.signal(signal.SIGALRM,
                                                raise_timeout)

    def _restore_alarm_handler(self):
        signal.signal(signal.SIGALRM, self._old_alarm_handler)
