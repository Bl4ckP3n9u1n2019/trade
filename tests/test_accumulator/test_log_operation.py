"""Tests the logging of Operation objects."""

from __future__ import absolute_import
import unittest

import trade


class TestLogOperation(unittest.TestCase):

    def setUp(self):
        self.asset = trade.Asset()
        self.accumulator = trade.Accumulator(self.asset, logging=True)

    def test_log_first_operation(self):
        operation = trade.Operation(
            quantity=100,
            price=10,
            asset=self.asset,
            date='2015-01-01'
        )
        self.accumulator.accumulate_operation(operation)
        expected_log = {
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [operation]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)

    def test_log_keys(self):
        operation = trade.Operation(
            quantity=100,
            price=10,
            asset=self.asset,
            date='2015-01-01'
        )
        self.accumulator.accumulate_operation(operation)
        self.assertEqual(list(self.accumulator.log), ['2015-01-01'])

    def test_returned_result(self):
        operation = trade.Operation(
            quantity=100,
            price=10,
            asset=self.asset,
            date='2015-01-01'
        )
        result = self.accumulator.accumulate_operation(operation)
        self.assertEqual(result, {})
