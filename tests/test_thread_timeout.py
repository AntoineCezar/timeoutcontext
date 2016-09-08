# -*- coding: utf-8 -*-

import sys
import time

from mock import patch

from timeoutcontext.thread_timeout import (
    ThreadTimeout,
)
if sys.version_info < (3, 3):
    from timeoutcontext import TimeoutError

from .base_test_case import BaseTestCase


class TestTimeoutAsAContextManager(BaseTestCase):

    def test_it_raise_timeout_exception_when_time_is_out(self):
        with self.assertRaises(TimeoutError):
            with ThreadTimeout(1):
                time.sleep(2)

    def test_it_does_not_raise_timeout_exception_when_time_is_not_out(self):
        with self.assertNotRaises(TimeoutError):
            with ThreadTimeout(2):
                time.sleep(1)

    def test_it_does_not_timeout_when_given_time_is_none(self):
        with self.assertNotRaises(TimeoutError):
            with ThreadTimeout(None):
                time.sleep(1)


class TestTimeoutAsADecorator(BaseTestCase):

    def test_it_raise_timeout_exception_when_time_is_out(self):
        @ThreadTimeout(1)
        def decorated():
            time.sleep(2)

        with self.assertRaises(TimeoutError):
            decorated()

    def test_it_does_not_raise_timeout_exception_when_time_is_not_out(self):
        @ThreadTimeout(2)
        def decorated():
            time.sleep(1)

        with self.assertNotRaises(TimeoutError):
            decorated()
