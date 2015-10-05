"""Tests for the utils functions."""

from __future__ import absolute_import
import unittest

import trade


class TestSameSign(unittest.TestCase):
    """Test the same_sign() function.

    This function should return True if the two values
    have opposite signs, and False otherwise.
    """

    def test_same_signs(self):
        self.assertTrue(trade.same_sign(-1, -4))

    def test_opposite_signs(self):
        self.assertFalse(trade.same_sign(-1, 4))


class TestAveragePrice(unittest.TestCase):
    """Test the function average_price.

    This function receives two quantity values, both with a
    price associeated to it, and returns the average price.
    """

    def setUp(self):
        pass

    def test_case_00(self):
        price = trade.average_price(10, 2, 10, 4)
        self.assertEqual(price, 3)

    def test_case_01(self):
        price = trade.average_price(10, 1, 10, 2)
        self.assertEqual(price, 1.5)

    def test_case_02(self):
        price = trade.average_price(10, 1, 10, 3)
        self.assertEqual(price, 2)


class TestDaytradeCondition(unittest.TestCase):
    """Tests the function daytrade_condition().

    The daytrade_condition function receives two operations and
    shoul return True if the two operations configure a daytrade,
    False otherwise.
    """

    def setUp(self):
        self.asset1 = trade.Asset()
        self.asset2 = trade.Asset()

    def test_case_00(self):
        operation1 = trade.Operation(
            quantity=-10,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        operation2 = trade.Operation(
            quantity=10,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        self.assertTrue(
            trade.plugins.daytrade_condition(operation1, operation2)
        )

    def test_case_01(self):
        operation1 = trade.Operation(
            quantity=10,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        operation2 = trade.Operation(
            quantity=-10,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        self.assertTrue(
            trade.plugins.daytrade_condition(operation1, operation2)
        )

    def test_case_02(self):
        operation1 = trade.Operation(
            quantity=0,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        operation2 = trade.Operation(
            quantity=0,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        self.assertFalse(
            trade.plugins.daytrade_condition(operation1, operation2)
        )

    def test_case_03(self):
        operation1 = trade.Operation(
            quantity=0,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        operation2 = trade.Operation(
            quantity=-10,
            price=5,
            date='2015-09-22',
            asset=self.asset2
        )
        self.assertFalse(
            trade.plugins.daytrade_condition(operation1, operation2)
        )

    def test_case_04(self):
        operation1 = trade.Operation(
            quantity=-10,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        operation2 = trade.Operation(
            quantity=0,
            price=5,
            date='2015-09-22',
            asset=self.asset2
        )
        self.assertFalse(
            trade.plugins.daytrade_condition(operation1, operation2)
        )

    def test_case_05(self):
        operation1 = trade.Operation(
            quantity=10,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        operation2 = trade.Operation(
            quantity=0,
            price=5,
            date='2015-09-22',
            asset=self.asset2
        )
        self.assertFalse(
            trade.plugins.daytrade_condition(operation1, operation2)
        )

    def test_case_06(self):
        operation1 = trade.Operation(
            quantity=0,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        operation2 = trade.Operation(
            quantity=10,
            price=5,
            date='2015-09-22',
            asset=self.asset2
        )
        self.assertFalse(
            trade.plugins.daytrade_condition(operation1, operation2)
        )

    def test_case_07(self):
        operation1 = trade.Operation(
            quantity=-10,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        operation2 = trade.Operation(
            quantity=-10,
            price=5,
            date='2015-09-22',
            asset=self.asset2
        )
        self.assertFalse(
            trade.plugins.daytrade_condition(operation1, operation2)
        )

    def test_case_08(self):
        operation1 = trade.Operation(
            quantity=10,
            price=5,
            date='2015-09-22',
            asset=self.asset1
        )
        operation2 = trade.Operation(
            quantity=10,
            price=5,
            date='2015-09-22',
            asset=self.asset2
        )
        self.assertFalse(
            trade.plugins.daytrade_condition(operation1, operation2)
        )


class TestFindPurchaseAndSale(unittest.TestCase):
    """Test the find_purchase_and_sale() function.

    This function receives two operations an is expected to
    return a tuple with the two operations: the purchase operation
    first as the first element and the sale operation as the second
    element.
    """

    def setUp(self):
        self.asset = trade.Asset()

    def test_case_00(self):
        operation1 = trade.Operation(
            quantity=10,
            price=5,
            date='2015-09-22',
            asset=self.asset
        )
        operation2 = trade.Operation(
            quantity=-10,
            price=5,
            date='2015-09-22',
            asset=self.asset
        )
        result = (operation1, operation2)
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(operation1, operation2),
            result
        )

    def test_case_01(self):
        operation1 = trade.Operation(
            quantity=-10,
            price=5,
            date='2015-09-22',
            asset=self.asset
        )
        operation2 = trade.Operation(
            quantity=10,
            price=5,
            date='2015-09-22',
            asset=self.asset
        )
        result = (operation2, operation1)
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(operation1, operation2),
            result
        )

    def test_case_02(self):
        operation1 = trade.Operation(
            quantity=10,
            price=5,
            date='2015-09-22',
            asset=self.asset
        )
        operation2 = trade.Operation(
            quantity=10,
            price=5,
            date='2015-09-22',
            asset=self.asset
        )
        result = None, None
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(operation1, operation2),
            result
        )

    def test_case_03(self):
        operation1 = trade.Operation(
            quantity=-10,
            price=5,
            date='2015-09-22',
            asset=self.asset
        )
        operation2 = trade.Operation(
            quantity=-10,
            price=5,
            date='2015-09-22',
            asset=self.asset
        )
        result = None, None
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(operation1, operation2),
            result
        )

    def test_case_04(self):
        operation1 = trade.Operation(
            quantity=0,
            price=0,
            date='2015-09-22',
            asset=self.asset
        )
        operation2 = trade.Operation(
            quantity=5,
            price=5,
            date='2015-09-22',
            asset=self.asset
        )
        result = None, None
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(operation1, operation2),
            result
        )

    def test_case_05(self):
        operation1 = trade.Operation(
            quantity=0,
            price=0,
            date='2015-09-22',
            asset=self.asset
        )
        operation2 = trade.Operation(
            quantity=-5,
            price=5,
            date='2015-09-22',
            asset=self.asset
        )
        result = (operation1, operation2)
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(operation1, operation2),
            result
        )

    def test_case_06(self):
        operation1 = trade.Operation(
            quantity=5,
            price=0,
            date='2015-09-22',
            asset=self.asset
        )
        operation2 = trade.Operation(
            quantity=0,
            price=5,
            date='2015-09-22',
            asset=self.asset
        )
        result = None, None
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(operation1, operation2),
            result
        )

    def test_case_07(self):
        operation1 = trade.Operation(
            quantity=-5,
            price=0,
            date='2015-09-22',
            asset=self.asset
        )
        operation2 = trade.Operation(
            quantity=0,
            price=5,
            date='2015-09-22',
            asset=self.asset
        )
        result = (operation2, operation1)
        self.assertEqual(
            trade.plugins.find_purchase_and_sale(operation1, operation2),
            result
        )
