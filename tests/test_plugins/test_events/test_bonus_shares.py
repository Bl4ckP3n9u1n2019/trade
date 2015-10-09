"""Tests for BonusShares events."""

from __future__ import absolute_import
import unittest

import trade

from tests.fixtures.assets import ASSET
from tests.fixtures.events import EVENT6, EVENT7, EVENT8


class TestBonusShares(unittest.TestCase):

    def setUp(self):
        self.accumulator = trade.Accumulator(ASSET, logging=True)
        self.accumulator.data['quantity'] = 100
        self.accumulator.data['price'] = 10
        self.accumulator.data['results'] = {'trades': 1200}


class TestBonusSharesCase00(TestBonusShares):
    """Test a bonus shares event with factor 1."""

    def setUp(self):
        super(TestBonusSharesCase00, self).setUp()
        self.accumulator.accumulate(EVENT6)

    def test_check_quantity(self):
        self.assertEqual(self.accumulator.data['quantity'], 200)

    def test_check_price(self):
        self.assertEqual(self.accumulator.data['price'], 5)

    def test_check_results(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 1200})


class TestBonusSharesCase01(TestBonusShares):
    """Test a bonus shares event with factor 2."""

    def setUp(self):
        super(TestBonusSharesCase01, self).setUp()
        self.accumulator.accumulate(EVENT8)

    def test_check_quantity(self):
        self.assertEqual(self.accumulator.data['quantity'], 300)

    def test_check_price(self):
        self.assertEqual(round(self.accumulator.data['price'], 2), 3.33)

    def test_check_results(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 1200})


class TestBonusSharesCase02(TestBonusShares):
    """Test a bonus shares event with factor 0.5."""

    def setUp(self):
        super(TestBonusSharesCase02, self).setUp()
        self.accumulator.accumulate(EVENT7)

    def test_check_quantity(self):
        self.assertEqual(self.accumulator.data['quantity'], 150)

    def test_check_price(self):
        self.assertEqual(round(self.accumulator.data['price'], 2), 6.67)

    def test_check_results(self):
        self.assertEqual(self.accumulator.data['results'], {'trades': 1200})
