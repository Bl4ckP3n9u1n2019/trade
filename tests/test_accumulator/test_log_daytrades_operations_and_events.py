"""Tests the logging of Operation, Daytrade and Event objects."""

from __future__ import absolute_import
import unittest

import trade
import trade.plugins


ASSET = trade.Asset()
DAYTRADE = trade.plugins.Daytrade(
    trade.Operation(
        asset=ASSET,
        quantity=100,
        price=10,
        date='2015-01-01'
    ),
    trade.Operation(
        asset=ASSET,
        quantity=-100,
        price=20,
        date='2015-01-01'
    )
)

DAYTRADE2 = trade.plugins.Daytrade(
    trade.Operation(
        asset=ASSET,
        quantity=100,
        price=10,
        date='2015-01-02'
    ),
    trade.Operation(
        asset=ASSET,
        quantity=-100,
        price=20,
        date='2015-01-02'
    )
)

OPERATION1 = trade.Operation(
    quantity=100,
    price=10,
    asset=ASSET,
    date='2015-01-01'
)
OPERATION2 = trade.Operation(
    quantity=100,
    price=10,
    asset=ASSET,
    date='2015-01-02'
)


class TestEvent(trade.plugins.Event):
    """A dummy event for the tests."""
    def update_container(self, container):
        pass


class TestLogDaytradesOperationsAndEventsCase00(unittest.TestCase):
    """Test logging events, operations and daytrades on the same date."""

    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(DAYTRADE)
        self.accumulator.accumulate_occurrence(OPERATION1)
        self.event = TestEvent(
            asset=ASSET,
            date='2015-01-01',
            factor=1
        )
        self.accumulator.accumulate_occurrence(self.event)

    def test_log(self):
        expected_log = {
            '2015-01-01': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [DAYTRADE, OPERATION1, self.event]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)


class TestLogDaytradesOperationsAndEventsCase01(unittest.TestCase):
    """Test logging all objects on the different dates."""

    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(DAYTRADE)
        self.accumulator.accumulate_occurrence(OPERATION2)
        self.event = TestEvent(
            asset=ASSET,
            date='2015-01-03',
            factor=1
        )
        self.accumulator.accumulate_occurrence(self.event)

    def test_log(self):
        expected_log = {
            '2015-01-03': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [self.event]
            },
            '2015-01-02': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [OPERATION2]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 0,
                    'price': 0
                },
                'occurrences': [DAYTRADE]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)


class TestLogDaytradesOperationsAndEventsCase02(unittest.TestCase):
    """Test logging objects on different dates."""

    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET, logging=True)
        self.accumulator.accumulate_occurrence(DAYTRADE)
        self.accumulator.accumulate_occurrence(OPERATION2)
        self.accumulator.accumulate_occurrence(DAYTRADE2)
        self.event = TestEvent(
            asset=ASSET,
            date='2015-01-02',
            factor=1
        )
        self.accumulator.accumulate_occurrence(self.event)

    def test_log(self):

        expected_log = {
            '2015-01-02': {
                'position': {
                    'quantity': 100,
                    'price': 10
                },
                'occurrences': [OPERATION2, DAYTRADE2, self.event]
            },
            '2015-01-01': {
                'position': {
                    'quantity': 0,
                    'price': 0
                },
                'occurrences': [DAYTRADE]
            }
        }
        self.assertEqual(self.accumulator.log, expected_log)
