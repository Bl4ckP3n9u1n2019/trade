"""Test the identification of Daytrades among Operations."""

from __future__ import absolute_import
import unittest

import trade


TASKS = [
    trade.plugins.fetch_exercises,
    trade.plugins.fetch_daytrades,
]


class TestContainerIndentifyDaytradesCase00(unittest.TestCase):
    """Test the identification of daytrade operations."""

    def setUp(self):
        self.asset = trade.Asset(symbol='some asset')
        self.trade1 = trade.Operation(
            date='2015-09-21',
            asset=self.asset,
            quantity=10,
            price=2
        )
        self.trade2 = trade.Operation(
            date='2015-09-21',
            asset=self.asset,
            quantity=-10,
            price=3
        )
        self.container = trade.OperationContainer(
            operations=[self.trade1, self.trade2])
        self.container.tasks = TASKS
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertTrue('operations' not in self.container.positions)

    def test_daytrades_len(self):
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 1)

    def test_daytrade_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset.symbol]\
                .asset.symbol,
            self.asset.symbol
        )

    def test_daytrade_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset.symbol].quantity,
            10
        )

    def test_daytrade_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset.symbol]\
                .operations[0].quantity,
            10
        )

    def test_daytrade_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset.symbol]\
                .operations[1].quantity,
            -10
        )

    def test_daytrade_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset.symbol]\
                .results,
            {'daytrades': 10}
        )


class TestContainerIndentifyDaytradesCase01(unittest.TestCase):
    """Test the identification of daytrade operations."""

    def setUp(self):
        self.asset = trade.Asset(symbol='some asset')
        self.trade1 = trade.Operation(
            date='2015-09-21',
            asset=self.asset,
            quantity=10,
            price=2
        )
        self.trade2 = trade.Operation(
            date='2015-09-21',
            asset=self.asset,
            quantity=-5,
            price=3
        )
        self.container = trade.OperationContainer(
            operations=[self.trade1, self.trade2])
        self.container.tasks = TASKS
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)

    def test_operations0_asset(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset.symbol]\
                .asset.symbol,
            self.asset.symbol
        )

    def test_operations1_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset.symbol].quantity,
            5
        )

    def test_operations1_price(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset.symbol].price,
            2
        )

    def test_daytrades_len(self):
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 1)

    def test_daytrade_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset.symbol]\
                .asset.symbol,
            self.asset.symbol
        )

    def test_daytrade_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset.symbol].quantity,
            5
        )

    def test_daytrade_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset.symbol].results,
            {'daytrades': 5}
        )


class TestContainerIndentifyDaytradesCase02(unittest.TestCase):
    """Test the identification of daytrade operations."""

    def setUp(self):
        self.asset1 = trade.Asset(symbol='some asset')
        self.asset2 = trade.Asset(symbol='some other asset')
        trade1 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=10,
            price=2
        )
        trade2 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=-5,
            price=3
        )
        trade3 = trade.Operation(
            date='2015-09-21',
            asset=self.asset2,
            quantity=-5,
            price=7
        )
        self.container = trade.OperationContainer(
            operations=[trade1, trade2, trade3])
        self.container.tasks = TASKS
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 2)

    def test_operations0_asset(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset1.symbol]\
                .asset.symbol,
            self.asset1.symbol
        )

    def test_operations0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset1.symbol]\
                .quantity,
            5
        )

    def test_operations0_price(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset1.symbol]\
                .price,
            2
        )

    def test_operations1_asset(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset2.symbol]\
                .asset.symbol,
            self.asset2.symbol
        )

    def test_operations1_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset2.symbol]\
                .quantity,
            -5
        )

    def test_common_trades1_price(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset2.symbol].price,
            7
        )

    def test_daytrades_len(self):
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 1)

    def test_daytrade_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .asset.symbol,
            self.asset1.symbol
        )

    def test_daytrade_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol].quantity,
            5
        )

    def test_daytrade_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol].results,
            {'daytrades': 5}
        )


class TestContainerIndentifyDaytradesCase03(unittest.TestCase):
    """Test the identification of daytrade operations."""

    def setUp(self):
        self.asset1 = trade.Asset(symbol='some asset')
        self.asset2 = trade.Asset(symbol='some other asset')
        trade1 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=10,
            price=2
        )
        trade2 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=-5,
            price=3
        )
        trade3 = trade.Operation(
            date='2015-09-21',
            asset=self.asset2,
            quantity=-5,
            price=7
        )
        trade4 = trade.Operation(
            date='2015-09-21',
            asset=self.asset2,
            quantity=5,
            price=10
        )
        self.container = trade.OperationContainer(
            operations=[trade1, trade2, trade3, trade4])
        self.container.tasks = TASKS
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)

    def test_common_trades0_asset(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset1.symbol]\
                .asset.symbol,
            self.asset1.symbol
        )

    def test_common_trades0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset1.symbol]\
                .quantity,
            5
        )

    def test_common_trades0_price(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset1.symbol].price,
            2
        )

    def test_daytrades_len(self):
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 2)

    def test_daytrade0_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .asset.symbol,
            self.asset1.symbol
        )

    def test_daytrade0_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .quantity,
            5
        )

    def test_daytrade0_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade0_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade0_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade0_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol].results,
            {'daytrades': 5}
        )

    def test_daytrade1_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .asset.symbol,
            self.asset2.symbol
        )

    def test_daytrade1_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol].quantity,
            5
        )

    def test_daytrade1_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade1_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol].results,
            {'daytrades': -15}
        )


class TestContainerIndentifyDaytradesCase04(unittest.TestCase):
    """Test the identification of daytrade operations."""

    def setUp(self):
        self.asset1 = trade.Asset(symbol='some asset')
        self.asset2 = trade.Asset(symbol='some other asset')
        trade1 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=10,
            price=2
        )
        trade2 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=-5,
            price=3
        )
        trade3 = trade.Operation(
            date='2015-09-21',
            asset=self.asset2,
            quantity=-5,
            price=7
        )
        trade4 = trade.Operation(
            date='2015-09-21',
            asset=self.asset2,
            quantity=5,
            price=10
        )
        trade5 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=-5,
            price=3
        )
        self.container = trade.OperationContainer(
            operations=[trade1, trade2, trade3, trade4, trade5])
        self.container.tasks = TASKS
        self.container.fetch_positions()

    def test_for_no_common_trades(self):
        self.assertTrue('operations' not in self.container.positions)

    def test_daytrades_len(self):
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 2)

    def test_daytrade0_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .asset.symbol,
            self.asset1.symbol
        )

    def test_daytrade0_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol].quantity,
            10
        )

    def test_daytrade0_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[0].quantity,
            10
        )

    def test_daytrade0_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade0_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[1].quantity,
            -10
        )

    def test_daytrade0_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .results,
            {'daytrades': 10}
        )

    def test_daytrade1_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .asset.symbol,
            self.asset2.symbol
        )

    def test_daytrade1_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .quantity,
            5
        )

    def test_daytrade1_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade1_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .results,
            {'daytrades': -15}
        )


class TestContainerIndentifyDaytradesCase05(unittest.TestCase):
    """Test the identification of daytrade operations."""

    def setUp(self):
        self.asset1 = trade.Asset(symbol='some asset')
        self.asset2 = trade.Asset(symbol='some other asset')
        trade1 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=10,
            price=2
        )
        trade2 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=-5,
            price=10
        )
        trade3 = trade.Operation(
            date='2015-09-21',
            asset=self.asset2,
            quantity=-5,
            price=7
        )
        trade4 = trade.Operation(
            date='2015-09-21',
            asset=self.asset2,
            quantity=5,
            price=10
        )
        trade5 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=-5,
            price=20
        )
        self.container = trade.OperationContainer(
            operations=[trade1, trade2, trade3, trade4, trade5])
        self.container.tasks = TASKS
        self.container.fetch_positions()

    def test_for_no_common_trades(self):
        self.assertTrue('operations' not in self.container.positions)

    def test_daytrades_len(self):
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 2)

    def test_check_daytrade0_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol].asset,
            self.asset1
        )

    def test_daytrade0_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol].quantity,
            10
        )

    def test_daytrade0_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[0].quantity,
            10
        )

    def test_daytrade0_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[1].price,
            15
        )

    def test_daytrade0_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[1].quantity,
            -10
        )

    def test_daytrade0_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol].results,
            {'daytrades': 130}
        )

    def test_check_daytrade1_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .asset.symbol,
            self.asset2.symbol
        )

    def test_daytrade1_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol].quantity,
            5
        )

    def test_daytrade1_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade1_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol].results,
            {'daytrades': -15}
        )


class TestContainerIndentifyDaytradesCase06(unittest.TestCase):
    """Test the identification of daytrade operations."""

    def setUp(self):
        self.asset1 = trade.Asset(symbol='some asset')
        self.asset2 = trade.Asset(symbol='some other asset')
        trade1 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=10,
            price=2
        )
        trade2 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=-5,
            price=3
        )
        trade3 = trade.Operation(
            date='2015-09-21',
            asset=self.asset2,
            quantity=-5,
            price=7
        )
        trade4 = trade.Operation(
            date='2015-09-21',
            asset=self.asset2,
            quantity=5,
            price=10
        )
        trade5 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=5,
            price=4
        )
        self.container = trade.OperationContainer(
            operations=[trade1, trade2, trade3, trade4, trade5])
        self.container.tasks = TASKS
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)

    def test_common_trades0_asset(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset1.symbol]\
                .asset.symbol,
            self.asset1.symbol
        )

    def test_common_trades0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset1.symbol]\
                .quantity,
            10
        )

    def test_common_trades0_price(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset1.symbol].price,
            3
        )

    def test_daytrades_len(self):
        self.assertEqual(
            len(self.container.positions['daytrades'].keys()),
            2
        )

    def test_daytrade0_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .asset.symbol,
            self.asset1.symbol
        )

    def test_daytrade0_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol].quantity,
            5
        )

    def test_daytrade0_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade0_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade0_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade0_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol].results,
            {'daytrades': 5}
        )

    def test_check_daytrade1_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .asset.symbol,
            self.asset2.symbol
        )

    def test_daytrade1_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol].quantity,
            5
        )

    def test_daytrade1_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade1_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol].results,
            {'daytrades': -15}
        )


class TestContainerIndentifyDaytradesCase07(unittest.TestCase):
    """Test the identification of daytrade operations."""

    def setUp(self):
        self.asset1 = trade.Asset(symbol='some asset')
        self.asset2 = trade.Asset(symbol='some other asset')
        self.asset3 = trade.Asset(symbol='even other asset')
        trade1 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=10,
            price=2
        )
        trade2 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=-5,
            price=3
        )
        trade3 = trade.Operation(
            date='2015-09-21',
            asset=self.asset2,
            quantity=-5,
            price=7
        )
        trade4 = trade.Operation(
            date='2015-09-21',
            asset=self.asset2,
            quantity=5,
            price=10
        )
        trade5 = trade.Operation(
            date='2015-09-21',
            asset=self.asset1,
            quantity=5,
            price=4
        )
        trade6 = trade.Operation(
            date='2015-09-21',
            asset=self.asset3,
            quantity=5,
            price=4
        )
        trade7 = trade.Operation(
            date='2015-09-21',
            asset=self.asset3,
            quantity=-5,
            price=2
        )
        trade8 = trade.Operation(
            date='2015-09-21',
            asset=self.asset3,
            quantity=5,
            price=4
        )
        trade9 = trade.Operation(
            date='2015-09-21',
            asset=self.asset3,
            quantity=-5,
            price=4
        )
        self.container = trade.OperationContainer(
            operations=[
                trade1, trade2, trade3, trade4, trade5,
                trade6, trade7, trade8, trade9
            ]
        )
        self.container.tasks = TASKS
        self.container.fetch_positions()

    def test_common_trades_len(self):
        self.assertEqual(len(self.container.positions['operations'].keys()), 1)

    def test_operations0_asset(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset1.symbol]\
                .asset.symbol,
            self.asset1.symbol
        )

    def test_operations0_quantity(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset1.symbol]\
                .quantity,
            10
        )

    def test_operations0_price(self):
        self.assertEqual(
            self.container.positions['operations'][self.asset1.symbol].price,
            3
        )

    def test_daytrades_len(self):
        self.assertEqual(
            len(self.container.positions['daytrades'].keys()),
            3
        )

    def test_daytrade0_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .asset.symbol,
            self.asset1.symbol
        )

    def test_daytrade0_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol].quantity,
            5
        )

    def test_daytrade0_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade0_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade0_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade0_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1.symbol].results,
            {'daytrades': 5}
        )

    def test_daytrade1_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .asset.symbol,
            self.asset2.symbol
        )

    def test_daytrade1_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol].quantity,
            5
        )

    def test_daytrade1_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol]\
                .operations[1].quantity,
            -5
        )

    def test_daytrade1_result(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2.symbol].results,
            {'daytrades': -15}
        )

    def test_daytrade2_asset(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3.symbol]\
                .asset.symbol,
            self.asset3.symbol
        )

    def test_daytrade2_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3.symbol].quantity,
            10
        )

    def test_daytrade2_buy_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3.symbol]\
                .operations[0].price,
            4
        )

    def test_daytrade2_buy_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3.symbol]\
                .operations[0].quantity,
            10
        )

    def test_daytrade2_sale_price(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3.symbol]\
                .operations[1].price,
            3
        )

    def test_daytrade2_sale_quantity(self):
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3.symbol]\
                .operations[1].quantity,
            -10
        )
