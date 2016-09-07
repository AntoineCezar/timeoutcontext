# -*- coding: utf-8 -*-
import sys
import pkg_resources

from .signal_timeout import SignalTimeout as timeout
if sys.version_info < (3, 3):
    from .timeout_error import TimeoutError


__version__ = pkg_resources.get_distribution(__package__).version

__all__ = [
    'timeout',
    'TimeoutError',
]
