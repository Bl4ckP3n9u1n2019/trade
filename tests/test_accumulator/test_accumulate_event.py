"""Tests the method accumulate_occurrence() of the Accumulator."""

from __future__ import absolute_import
from __future__ import division

import unittest

import trade
import trade.plugins


class EventThatChangeResults(trade.plugins.Event):
    """A fictional event for the tests."""

    def update_container(self, container):
        for key in container.results.keys():
            container.results[key] += self.factor


class TestEventThatChangeResultsCase00(unittest.TestCase):
    """Test the accumulation of an Event object.

    In this test we use the EventThatChangeResults object
    to test the consequences of an Event accumulation.
    """
    def setUp(self):
        self.asset = trade.Asset()
        self.accumulator = trade.Accumulator(self.asset)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}
        self.event = EventThatChangeResults(self.asset, '2015-09-27', 2)

    def test_check_initial_quantity(self):
        self.assertEqual(self.accumulator.quantity, 100)

    def test_check_initial_price(self):
        self.assertEqual(self.accumulator.price, 10)

    def test_check_initial_results(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})

    def test_check_quantity_after_split(self):
        self.accumulator.accumulate_occurrence(self.event)
        self.assertEqual(self.accumulator.quantity, 100)

    def test_check_price_after_split(self):
        self.accumulator.accumulate_occurrence(self.event)
        self.assertEqual(self.accumulator.price, 10)

    def test_check_results_after_split(self):
        self.accumulator.accumulate_occurrence(self.event)
        self.assertEqual(self.accumulator.results, {'trades': 1202})
