"""Tests the logging of Operation, Daytrade and Event objects."""

from __future__ import absolute_import
import unittest

import trade
import trade.plugins


class TestEvent(trade.Event):
    def update_portfolio(self, container):
        pass


class TestLogDaytradesOperationsAndEvents_Case_00(unittest.TestCase):
    """Test logging events, operations and daytrades on the same date."""

    def setUp(self):
        self.asset = trade.Asset()
        self.accumulator = trade.Accumulator(self.asset, logging=True)

    def test_log(self):
        daytrade = trade.plugins.Daytrade(
            date='2015-01-01',
            asset=self.asset,
            quantity=100,
            purchase_price=10,
            sale_price=20
        )
        self.accumulator.accumulate_operation(daytrade)

        operation = trade.Operation(
            quantity=100,
            price=10,
            asset=self.asset,
            date='2015-01-01'
        )
        self.accumulator.accumulate_operation(operation)

        event = TestEvent(
            asset=self.asset,
            date='2015-01-01'
        )
        self.accumulator.accumulate_event(event)

        expected_log = {
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [daytrade, operation, event]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)


class TestLogDaytradesOperationsAndEvents_Case_01(unittest.TestCase):
    """Test logging all objects on the different dates."""

    def setUp(self):
        self.asset = trade.Asset()
        self.accumulator = trade.Accumulator(self.asset, logging=True)

    def test_log(self):
        daytrade = trade.plugins.Daytrade(
            date='2015-01-01',
            asset=self.asset,
            quantity=100,
            purchase_price=10,
            sale_price=20
        )
        self.accumulator.accumulate_operation(daytrade)

        operation = trade.Operation(
            quantity=100,
            price=10,
            asset=self.asset,
            date='2015-01-02'
        )
        self.accumulator.accumulate_operation(operation)

        event = TestEvent(
            asset=self.asset,
            date='2015-01-03'
        )
        self.accumulator.accumulate_event(event)

        expected_log = {
            '2015-01-03': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [event]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [operation]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 0,
                    'price': 0
                },
                'occurrences': [daytrade]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)


class TestLogDaytradesOperationsAndEvents_Case_02(unittest.TestCase):
    """Test logging objects on different dates."""

    def setUp(self):
        self.asset = trade.Asset()
        self.accumulator = trade.Accumulator(self.asset, logging=True)

    def test_log(self):
        daytrade = trade.plugins.Daytrade(
            date='2015-01-01',
            asset=self.asset,
            quantity=100,
            purchase_price=10,
            sale_price=20
        )
        self.accumulator.accumulate_operation(daytrade)

        operation = trade.Operation(
            quantity=100,
            price=10,
            asset=self.asset,
            date='2015-01-02'
        )
        self.accumulator.accumulate_operation(operation)

        daytrade2 = trade.plugins.Daytrade(
            date='2015-01-02',
            asset=self.asset,
            quantity=100,
            purchase_price=10,
            sale_price=20
        )
        self.accumulator.accumulate_operation(daytrade2)

        event = TestEvent(
            asset=self.asset,
            date='2015-01-02'
        )
        self.accumulator.accumulate_event(event)

        expected_log = {
            '2015-01-02': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [operation, daytrade2, event]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 0,
                    'price': 0
                },
                'occurrences': [daytrade]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)
