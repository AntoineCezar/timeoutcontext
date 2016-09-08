# -*- coding: utf-8 -*-
import sys
import pkg_resources

from .signal_timeout import SignalTimeout
from .thread_timeout import ThreadTimeout

if sys.version_info < (3, 0):
    from timeout_error import TimeoutError
elif sys.version_info < (3, 3):
    from .timeout_error import TimeoutError

timeout = SignalTimeout

__version__ = pkg_resources.get_distribution(__package__).version

__all__ = [
    'SignalTimeout',
    'ThreadTimeout',
    'TimeoutError',
    'timeout',
]
