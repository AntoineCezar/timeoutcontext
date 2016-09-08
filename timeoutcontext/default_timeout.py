# -*- coding: utf-8 -*-
import sys

from .signal_timeout import SignalTimeout
from .thread_timeout import ThreadTimeout


def default_timeout(platform):
    if platform in ('win', 'cygwin'):
        return ThreadTimeout

    return SignalTimeout
