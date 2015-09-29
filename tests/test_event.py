from __future__ import absolute_import
import unittest

import trade


class TestBaseEventBehavior(unittest.TestCase):
    """Test the Event class and its default behavior.
    """

    def setUp(self):
        self.asset = trade.Asset()
        self.date = '2015-09-29'
        self.event = trade.Event(asset=self.asset, date=self.date)

    def test_event_should_exist(self):
        self.assertTrue(self.event)

    def test_event_asset(self):
        self.assertEqual(self.event.asset, self.asset)

    def test_event_date(self):
        self.assertEqual(self.event.date, self.date)

    def test_event_update_portfolio(self):
        expected_return = (10,1)
        self.assertEqual(self.event.update_portfolio(10,1,{}), expected_return)


class TestBaseEventAccumulation(unittest.TestCase):

    def setUp(self):
        self.asset = trade.Asset()
        self.date = '2015-09-29'
        self.accumulator = trade.Accumulator(self.asset)
        self.accumulator.quantity = 100
        self.accumulator.price = 10
        self.accumulator.results = {'trades': 1200}

    def test_check_initial_quantity(self):
        self.assertEqual(self.accumulator.quantity, 100)

    def test_check_initial_price(self):
        self.assertEqual(self.accumulator.price, 10)

    def test_check_initial_results(self):
        self.assertEqual(self.accumulator.results, {'trades': 1200})

    def test_check_quantity_after_event(self):
        event = trade.Event(asset=self.asset, date=self.date)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.quantity, 100)

    def test_check_price_after_event(self):
        event = trade.Event(asset=self.asset, date=self.date)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.price, 10)

    def test_check_results_after_event(self):
        event = trade.Event(asset=self.asset, date=self.date)
        self.accumulator.accumulate_event(event)
        self.assertEqual(self.accumulator.results, {'trades': 1200})
