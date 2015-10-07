"""Tests the logging of Operation objects."""

from __future__ import absolute_import
import unittest

import trade

from tests.fixtures.operations import ASSET, OPERATION18
from . fixture_logs import EXPECTED_LOG15


class TestLogOperation(unittest.TestCase):
    """Tests the logging of Operation objects."""

    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET, logging=True)
        self.accumulator.accumulate(OPERATION18)

    def test_log_first_operation(self):
        self.assertEqual(self.accumulator.log, EXPECTED_LOG15)

    def test_log_keys(self):
        self.assertEqual(list(self.accumulator.log), ['2015-01-01'])

    def test_returned_result(self):
        self.assertEqual(OPERATION18.results, {})
