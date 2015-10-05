"""Tests the creation of Operation objects."""

from __future__ import absolute_import
from __future__ import division
import unittest

import trade


class TestOperationCreation(unittest.TestCase):
    """Test the creation of Operation objects."""

    def setUp(self):
        asset = trade.Asset(symbol='AAPL')
        self.operation = trade.Operation(
            date='2015-09-18',
            asset=asset,
            quantity=20,
            price=10,
            commissions={'some discount': 3}
        )

    def test_trade_exists(self):
        self.assertTrue(self.operation)

    def test_trade_asset(self):
        self.assertEqual(self.operation.asset.symbol, 'AAPL')

    def test_trade_date(self):
        self.assertEqual(self.operation.date, '2015-09-18')

    def test_trade_quantity(self):
        self.assertEqual(self.operation.quantity, 20)

    def test_trade_price(self):
        self.assertEqual(self.operation.price, 10)

    def test_trade_discounts(self):
        discounts={'some discount': 3}
        self.assertEqual(self.operation.commissions, discounts)
