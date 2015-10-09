"""Tests the logging of Operation, Daytrade and Event objects."""

from __future__ import absolute_import
import unittest

import trade
import trade.plugins

from tests.fixtures.operations import (
    ASSET, OPERATION1, OPERATION18, DAYTRADE2, DAYTRADE3,
)
from tests.fixtures.events import (
    EVENT0, EVENT1, EVENT2,
)
from . fixture_logs import (
    EXPECTED_LOG19, EXPECTED_LOG20, EXPECTED_LOG21
)


class TestLogDaytradesOperationsAndEventsCase00(unittest.TestCase):
    """Test logging events, operations and daytrades on the same date."""

    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET, logging=True)
        self.accumulator.accumulate(DAYTRADE2)

    def test_log_case_00(self):
        self.accumulator.accumulate(OPERATION18)
        self.accumulator.accumulate(EVENT0)
        self.assertEqual(self.accumulator.log, EXPECTED_LOG19)

    def test_log_case_01(self):
        self.accumulator.accumulate(OPERATION1)
        self.accumulator.accumulate(EVENT1)
        self.assertEqual(self.accumulator.log, EXPECTED_LOG20)

    def test_log_case_02(self):
        self.accumulator.accumulate(OPERATION1)
        self.accumulator.accumulate(DAYTRADE3)
        self.accumulator.accumulate(EVENT2)
        self.assertEqual(self.accumulator.log, EXPECTED_LOG21)
