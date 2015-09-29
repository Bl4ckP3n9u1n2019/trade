from __future__ import absolute_import
import unittest

import trade as trade_tools


# TODO document this
# TODO more tests


class TestTradeContainerCreation_Case_00(unittest.TestCase):

    def setUp(self):
        self.container = trade_tools.OperationContainer()

    def test_trade_container_should_exist(self):
        self.assertTrue(self.container)


class TestTradeContainerCreation_Case_01(unittest.TestCase):

    def setUp(self):
        commissions = {
            'brokerage': 2.3,
            'other': 1
        }
        self.container = trade_tools.OperationContainer(
            commissions=commissions
        )

    def test_trade_container_should_exist(self):
        self.assertTrue(self.container)

    def test_trade_container_commissions(self):
        commissions = {
            'brokerage': 2.3,
            'other': 1
        }
        self.assertEqual(self.container.commissions, commissions)

class TestTradeContainerDefaultTaxManager(unittest.TestCase):

    def setUp(self):
        self.container = trade_tools.OperationContainer()

    def test_check_container_default_tax_manager(self):
        self.assertTrue(
            isinstance(self.container.tax_manager, trade_tools.TaxManager)
        )


class TestTradeContainer_add_to_common_operations(unittest.TestCase):

    def setUp(self):
        self.asset = trade_tools.Asset('some asset')
        trade = trade_tools.Operation(
                    date='2015-09-21', asset=self.asset, quantity=10, price=2)
        self.trade_container = \
                    trade_tools.OperationContainer(operations=[trade])
        self.trade_container.identify_daytrades_and_common_operations()
        trade = trade_tools.Operation(
                    date='2015-09-21', asset=self.asset, quantity=10, price=4)
        self.trade_container.add_to_common_operations(trade)

    def test_common_trades_len_should_be_1(self):
        self.assertEqual(len(self.trade_container.common_operations.keys()), 1)

    def test_daytrades_len_should_be_zero(self):
        self.assertEqual(len(self.trade_container.daytrades.keys()), 0)

    def test_common_trades0_quantity_should_be_20(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset].quantity,
            20
        )

    def test_common_trades0_price_should_be_3(self):
        self.assertEqual(
            self.trade_container.common_operations[self.asset].price,
            3
        )
