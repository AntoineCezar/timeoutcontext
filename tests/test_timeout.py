#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
from contextlib import contextmanager

from timeoutcontext import timeout
from timeoutcontext import TimeoutException


class BaseTestCase(unittest.TestCase):

    @contextmanager
    def assertNotRaises(self, exc_type):
        try:
            yield None
        except exc_type:
            raise self.failureException('{} raised'.format(exc_type.__name__))


class TestTimeoutAsAContextManager(BaseTestCase):

    def test_it_raise_timeout_exception_when_time_is_out(self):
        with self.assertRaises(TimeoutException):
            with timeout(1):
                time.sleep(2)

    def test_it_does_not_raise_timeout_exception_when_time_is_not_out(self):
        with self.assertNotRaises(TimeoutException):
            with timeout(2):
                time.sleep(1)

    def test_it_does_not_timeout_when_given_time_is_none(self):
        with self.assertNotRaises(TimeoutException):
            with timeout(None):
                time.sleep(1)


class TestTimeoutAsADecorator(BaseTestCase):

    def test_it_raise_timeout_exception_when_time_is_out(self):
        @timeout(1)
        def decorated():
            time.sleep(2)

        with self.assertRaises(TimeoutException):
            decorated()

    def test_it_does_not_raise_timeout_exception_when_time_is_not_out(self):
        @timeout(2)
        def decorated():
            time.sleep(1)

        with self.assertNotRaises(TimeoutException):
            decorated()
