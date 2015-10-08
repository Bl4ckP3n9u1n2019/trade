"""Test the properties of the Accumulator."""

from __future__ import absolute_import
import unittest
import copy

import trade

from tests.fixtures.operations import (
    OPERATION39, OPERATION40, OPERATION41
)


class TestContainerProperties(unittest.TestCase):
    """A base class with all operations used in the test cases."""

    def setUp(self):
        pass


class TestContainerPropertiesCase02(TestContainerProperties):
    """Test the volume property of the Container."""

    def setUp(self):
        super(TestContainerPropertiesCase02, self).setUp()
        self.trade_container = trade.OperationContainer(
            operations=[
                copy.deepcopy(OPERATION39)
            ]
        )
        self.trade_container.fetch_positions()

    def test_volume(self):
        self.assertEqual(self.trade_container.volume, 20)


class TestContainerPropertiesCase03(TestContainerProperties):
    """Test the volume property of the Container."""

    def setUp(self):
        super(TestContainerPropertiesCase03, self).setUp()
        self.trade_container = trade.OperationContainer(
            operations=[
                copy.deepcopy(OPERATION39),
                copy.deepcopy(OPERATION40)
            ]
        )
        self.trade_container.fetch_positions()

    def test_volume(self):
        self.assertEqual(self.trade_container.volume, 25)


class TestContainerPropertiesCase05(TestContainerProperties):
    """Test the volume property of the Container."""

    def setUp(self):
        super(TestContainerPropertiesCase05, self).setUp()
        self.trade_container = trade.OperationContainer(
            operations=[
                copy.deepcopy(OPERATION39),
                copy.deepcopy(OPERATION40),
                copy.deepcopy(OPERATION41)
            ]
        )
        self.trade_container.fetch_positions()

    def test_volume(self):
        self.assertEqual(self.trade_container.volume, 125)
