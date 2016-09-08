# -*- coding: utf-8 -*-
import sys
import pkg_resources

from .signal_timeout import SignalTimeout
from .thread_timeout import ThreadTimeout
from .default_timeout import default_timeout

if sys.version_info < (3, 0):
    from timeout_error import TimeoutError
elif sys.version_info < (3, 3):
    from .timeout_error import TimeoutError

timeout = default_timeout(sys.platform)

__version__ = pkg_resources.get_distribution(__package__).version

__all__ = [
    'SignalTimeout',
    'ThreadTimeout',
    'TimeoutError',
    'timeout',
]
