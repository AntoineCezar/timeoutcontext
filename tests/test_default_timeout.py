# -*- coding: utf-8 -*-

import sys
import time
import unittest

from timeoutcontext.thread_timeout import ThreadTimeout
from timeoutcontext.signal_timeout import SignalTimeout
from timeoutcontext.default_timeout import default_timeout


class TestTimeout(unittest.TestCase):

    def test_returns_thread_timeout_when_win(self):
        self.assertIs(default_timeout('win'), ThreadTimeout)

    def test_returns_thread_timeout_when_cygwin(self):
        self.assertIs(default_timeout('cygwin'), ThreadTimeout)

    def test_returns_signal_timeout_otherwise(self):
        self.assertIs(default_timeout('anything else'), SignalTimeout)
