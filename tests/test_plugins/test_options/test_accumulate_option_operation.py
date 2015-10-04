from __future__ import absolute_import
import unittest

import trade


class Test_accumulate_option_operation_case_00(unittest.TestCase):
    """Accumulate a Option operation."""

    def setUp(self):
        self.asset = trade.Asset(name='Main')
        self.option = trade.plugins.Option(
            name='Option',
            expiration_date='2015-12-31',
            underlying_assets=[self.asset],
            ratio=1
        )

        # Accumulate a option operation
        self.operation = trade.Operation(
            quantity=100,
            price=10,
            asset=self.option,
            date='2015-01-01'
        )
        self.accumulator = trade.Accumulator(self.option)
        self.result = self.accumulator.accumulate_operation(self.operation)

    def test_returned_result(self):
        self.assertEqual(self.result, {})

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.price, 10)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 100)

    def test_accumulator_results(self):
        self.assertEqual(self.accumulator.results, {})
