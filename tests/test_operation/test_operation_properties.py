"""Tests the real_price property of Operation objects."""

from __future__ import absolute_import
from __future__ import division
import unittest
import copy

from tests.fixtures.commissions import (
    COMMISSIONS0, COMMISSIONS1, COMMISSIONS2, COMMISSIONS3, COMMISSIONS4,
    COMMISSIONS5, COMMISSIONS6, COMMISSIONS7, COMMISSIONS8
)
from tests.fixtures.operations import (
    OPERATION19, OPERATION55
)


class TestOperationProperties(unittest.TestCase):

    def setUp(self):
        self.operation1 = copy.deepcopy(OPERATION19)
        self.operation2 = copy.deepcopy(OPERATION55)


class TestOperationRealPrice(TestOperationProperties):
    """Test the real_price property of Operation objects.

    The real price of an operation (the real unitary price of the
    asset) if the operation's price with all rated commissions
    and taxes.
    """

    def test_price_no_discount(self):
        self.assertEqual(self.operation1.real_price, 10)

    def test_price_one_discount(self):
        self.operation1.commissions = COMMISSIONS0
        self.assertEqual(self.operation1.real_price, 10.15)

    def test_discounts_case1(self):
        self.operation1.commissions = COMMISSIONS1
        self.assertEqual(self.operation1.real_price, 10.2)

    def test_discounts_case2(self):
        self.operation1.commissions = COMMISSIONS2
        self.assertEqual(self.operation1.real_price, 10.3)

    def test_discounts_case3(self):
        self.operation1.commissions = COMMISSIONS3
        self.assertEqual(self.operation1.real_price, 10.15)

    def test_value_no_discount(self):
        self.assertEqual(self.operation1.real_value, 200)

    def test_value_one_discount(self):
        self.operation1.commissions = COMMISSIONS4
        self.assertEqual(self.operation1.real_value, 206)

    def test_value_case_1(self):
        self.operation1.commissions = COMMISSIONS5
        self.assertEqual(self.operation1.real_value, 208)

    def test_value_case_2(self):
        self.operation1.commissions = COMMISSIONS6
        self.assertEqual(self.operation1.real_value, 213)

    def test_value_case_3(self):
        self.operation1.commissions = COMMISSIONS7
        self.assertEqual(self.operation1.real_value, 205)


class TestOperationTotalDiscounts(TestOperationProperties):
    """Test the total_commissions property of Operation objects."""

    def test_one_discount(self):
        self.operation1.commissions = COMMISSIONS0
        self.assertEqual(self.operation1.total_commissions, 3)

    def test_discounts_case_1(self):
        self.operation1.commissions = COMMISSIONS1
        self.assertEqual(self.operation1.total_commissions, 4)

    def test_discounts_case_2(self):
        self.operation1.commissions = COMMISSIONS2
        self.assertEqual(self.operation1.total_commissions, 6)

    def test_discounts_case_3(self):
        self.operation1.commissions = COMMISSIONS3
        self.assertEqual(self.operation1.total_commissions, 3)


class TestOperationVolumeCase00(TestOperationProperties):
    """Test the volume property of Operation objects.

    The volume of the operation is its absolute quantity * its price.
    """

    def test_purchase(self):
        self.assertEqual(self.operation1.volume, 200)

    def test_sale(self):
        self.assertEqual(self.operation1.volume, 200)

    def test_sale_with_discounts(self):
        self.operation1.commissions = COMMISSIONS8
        self.operation1.fees = {
            'some tax': 0.005,
            'some other tax': 0.0275
        }
        self.assertEqual(self.operation1.volume, 200)
