from __future__ import absolute_import
import unittest

from trade import Accumulator as AssetAccumulator
from trade import Asset, Operation


# TODO document this
# TODO more tests


class Test_accumulate_operation_Case_00(unittest.TestCase):

    def setUp(self):
        self.asset = Asset()
        self.operation = Operation(100, 10, asset=self.asset, date='2015-01-01')
        self.accumulator = AssetAccumulator(self.asset, logging=True)
        self.result = self.accumulator.accumulate_operation(self.operation)

    def test_returned_result(self):
        self.assertEqual(self.result, {'trades': 0})


class Test_accumulate_operation_Case_01(unittest.TestCase):

    def setUp(self):
        self.asset0 = Asset()
        self.asset1 = Asset('other')
        self.operation = Operation(100, 10, asset=self.asset0, date='2015-01-01')
        self.accumulator = AssetAccumulator(self.asset1, logging=True)
        self.result = self.accumulator.accumulate_operation(self.operation)

    def test_returned_result(self):
        self.assertEqual(self.result, {'trades': 0})
