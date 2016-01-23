# -*- coding: utf-8 -*-

import sys
import signal
if sys.version_info < (3, 2):
    from contextdecorator import ContextDecorator
else:
    from contextlib import ContextDecorator


class TimeoutException(Exception):
    pass


def raise_timeout(signum, frame):
    raise TimeoutException()


class timeout(ContextDecorator):
    """Raises TimeoutException when the gien time in seconds elapsed.

        As a context manager:

            >>> from timeoutcontext import timeout, TimeoutException
            >>> from time import sleep
            >>>
            >>> try:
            ...     with timeout(1):
            ...         sleep(2)
            ... except TimeoutException:
            ...     print('timeout')
            ...
            timeout

        As a decorator:

            >>> from timeoutcontext import timeout, TimeoutException
            >>> from time import sleep
            >>>
            >>> @timeout(1)
            ... def wait():
            ...     sleep(2)
            ...
            >>> try:
            ...     wait()
            ... except TimeoutException:
            ...     print('timeout')
            ...
            timeout
    """

    def __init__(self, seconds):
        self._seconds = seconds

    def __enter__(self):
        if self._seconds:
            self._replace_alarm_handler()
            signal.alarm(self._seconds)
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
