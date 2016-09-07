#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest
import time
from contextlib import contextmanager

from mock import patch

from timeoutcontext.signal_timeout import (
    raise_timeout,
    SignalTimeout,
)
if sys.version_info < (3, 3):
    from timeoutcontext import TimeoutError


class BaseTestCase(unittest.TestCase):

    @contextmanager
    def assertNotRaises(self, exc_type):
        try:
            yield None
        except exc_type:
            raise self.failureException('{} raised'.format(exc_type.__name__))


class TestTimeoutAsAContextManager(BaseTestCase):

    def test_it_raise_timeout_exception_when_time_is_out(self):
        with self.assertRaises(TimeoutError):
            with SignalTimeout(1):
                time.sleep(2)

    def test_it_does_not_raise_timeout_exception_when_time_is_not_out(self):
        with self.assertNotRaises(TimeoutError):
            with SignalTimeout(2):
                time.sleep(1)

    def test_it_does_not_timeout_when_given_time_is_none(self):
        with self.assertNotRaises(TimeoutError):
            with SignalTimeout(None):
                time.sleep(1)

    @patch('timeoutcontext.signal_timeout.signal')
    def test_it_does_not_replace_alarm_handler_when_seconds_is_none(self, signal_mock):
            with SignalTimeout(None):
                signal_mock.signal.assert_not_called()

    @patch('timeoutcontext.signal_timeout.signal')
    def test_it_does_not_set_alarm_when_seconds_is_none(self, signal_mock):
            with SignalTimeout(None):
                signal_mock.alarm.assert_not_called()

    @patch('timeoutcontext.signal_timeout.signal')
    def test_it_does_not_restore_alarm_handler_when_seconds_is_none(self, signal_mock):
            with SignalTimeout(None):
                pass

            signal_mock.signal.assert_not_called()

    def test_it_does_not_timeout_when_given_time_is_zero(self):
        with self.assertNotRaises(TimeoutError):
            with SignalTimeout(0):
                time.sleep(1)

    @patch('timeoutcontext.signal_timeout.signal')
    def test_it_does_not_replace_alarm_handler_when_seconds_is_zero(self, signal_mock):
            with SignalTimeout(0):
                signal_mock.signal.assert_not_called()

    @patch('timeoutcontext.signal_timeout.signal')
    def test_it_does_not_set_alarm_when_seconds_is_zero(self, signal_mock):
            with SignalTimeout(0):
                signal_mock.alarm.assert_not_called()

    @patch('timeoutcontext.signal_timeout.signal')
    def test_it_does_not_restore_alarm_handler_when_seconds_is_zero(self, signal_mock):
            with SignalTimeout(0):
                pass

            signal_mock.signal.assert_not_called()

    @patch('timeoutcontext.signal_timeout.signal')
    def test_it_replace_alarm_handler_on_enter(self, signal_mock):
        with SignalTimeout(2):
            signal_mock.signal.assert_called_with(signal_mock.SIGALRM,
                                                  raise_timeout)

    @patch('timeoutcontext.signal_timeout.signal')
    def test_it_request_alarm_to_be_sent_in_given_seconds_on_enter(self, signal_mock):
        with SignalTimeout(2):
            signal_mock.alarm.assert_called_with(2)

    @patch('timeoutcontext.signal_timeout.signal')
    def test_it_restore_alarm_handler_on_exit(self, signal_mock):
        old_alarm_handler = signal_mock.signal()

        with SignalTimeout(2):
            pass

        signal_mock.signal.assert_called_with(signal_mock.SIGALRM,
                                              old_alarm_handler)

    @patch('timeoutcontext.signal_timeout.signal')
    def test_it_resets_alarm_on_exit(self, signal_mock):
        with SignalTimeout(2):
            pass

        signal_mock.alarm.assert_called_with(0)


class TestTimeoutAsADecorator(BaseTestCase):

    def test_it_raise_timeout_exception_when_time_is_out(self):
        @SignalTimeout(1)
        def decorated():
            time.sleep(2)

        with self.assertRaises(TimeoutError):
            decorated()

    def test_it_does_not_raise_timeout_exception_when_time_is_not_out(self):
        @SignalTimeout(2)
        def decorated():
            time.sleep(1)

        with self.assertNotRaises(TimeoutError):
            decorated()
