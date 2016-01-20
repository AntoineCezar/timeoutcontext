# -*- coding: utf-8 -*-
import pkg_resources

from ._timeout import timeout
from ._timeout import TimeoutException


__version__ = pkg_resources.get_distribution(__package__).version

__all__ = [
    'timeout',
    'TimeoutException',
]
