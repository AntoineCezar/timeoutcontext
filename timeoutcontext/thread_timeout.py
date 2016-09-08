# -*- coding: utf-8 -*-

import sys
from threading import Timer
try:
    import _thread as thread
except ImportError:
    import thread

if sys.version_info < (3, 2):
    from contextlib2 import ContextDecorator
else:
    from contextlib import ContextDecorator

if sys.version_info < (3, 0):
    from timeout_error import TimeoutError
elif sys.version_info < (3, 3):
    from .timeout_error import TimeoutError


class ThreadTimeout(ContextDecorator):
    """Raises TimeoutError when the gien time in seconds elapsed.

        As a context manager:

            >>> import sys
            >>> from time import sleep
            >>> from timeoutcontext import ThreadTimeout as timeout
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
            >>> from timeoutcontext import ThreadTimeout as timeout
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
        self._timer = Timer(self._seconds, thread.interrupt_main)
        self._timer.daemon = True

    def __enter__(self):
        if self._seconds:
            self._timer.start()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._timer.cancel()

        if exc_type == KeyboardInterrupt and not self._timer.is_alive():
            raise TimeoutError
