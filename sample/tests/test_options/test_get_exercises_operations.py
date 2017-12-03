"""Test the trade.plugins.fetch_exercises task from the Option plugin."""

from __future__ import absolute_import

import unittest
import copy
from trade_app.trade import trade
from trade_app.trade.container_tasks import (
    find_volume, fetch_daytrades, prorate_commissions, group_positions
)

from fixtures.operations import (
    EXERCISE_OPERATION2, EXERCISE_OPERATION3
)
from fixtures.assets import OPTION1


class TestFetchPositions(unittest.TestCase):
    """Create the default operations for the test cases."""

    commissions = {}
    operations = []
    positions = {}
    daytrades = {}
    exercises = {}
    volume = False

    def setUp(self):

        self.container = trade.OperationContainer(
            tasks=[
                find_volume,
                fetch_daytrades,
                group_positions,
            ],
            operations=copy.deepcopy(self.operations)
        )
        self.container.commissions = self.commissions
        self.container.fetch_positions()
        prorate_commissions(self.container)

        self.state = {
            'operations': self.positions,
            'exercises': self.exercises,
            'daytrades': self.daytrades
        }

    def test_container_volume(self):
        """Check the volume of the OperationContainer."""
        self.assertEqual(self.container.context['volume'], self.volume)

    def len_check(self, len_type):
        """Check the len of a type of position in the container."""
        if len_type in self.container.context['positions']:
            self.assertEqual(
                len(self.container.context['positions'][len_type].keys()),
                len(self.state[len_type].keys())
            )

    def state_check(self, position_type):
        """Check the state of a type of position in the container."""
        if 'positions' in self.container.context:
            if position_type in self.container.context['positions']:
                for position in self.container.context['positions'][position_type].values():
                    position_details = position.__dict__
                    for key in position_details:
                        if key in \
                            self.state[position_type][position.subject.symbol]:
                            self.assertEqual(
                                position_details[key],
                                self.state\
                                    [position_type][position.subject.symbol][key]
                            )

    def test_operations_len(self):
        """Check the len of the common operations positions."""
        self.len_check('operations')

    def test_operations_states(self):
        """Check the state of the common operations positions."""
        self.state_check('operations')

    def test_exercises_len(self):
        """Check the len of the exercise positions."""
        self.len_check('exercises')

    def test_exercise_states(self):
        """Check the state of the exercise positions."""
        self.state_check('exercises')

    def test_daytrades_len(self):
        """Check the len of the daytrade positions."""
        self.len_check('daytrades')

    def test_daytrades_states(self):
        """Check the state of the daytrade positions."""
        self.state_check('daytrades')

    def test_daytrades_buy_state(self):
        """Check the state of the daytrade positions purchases."""
        self.check_daytrade_suboperation(0, 'buy')

    def test_daytrades_sale_state(self):
        """Check the state of the daytrade positions sales."""
        self.check_daytrade_suboperation(1, 'sale')

    def check_daytrade_suboperation(self, operation_index, operation_type):
        """Check the state of the daytrade suboperations."""
        for asset in self.daytrades.keys():
            self.assertEqual(
                (
                    self.container.context['positions']['daytrades'][asset]\
                        .operations[operation_index].price,
                    self.container.context['positions']['daytrades'][asset]\
                        .operations[operation_index].quantity,
                    self.container.context['positions']['daytrades'][asset]\
                        .operations[operation_index].commissions,
                ),
                (
                    self.daytrades[asset][operation_type + ' price'],
                    self.daytrades[asset][operation_type + ' quantity'],
                    self.daytrades[asset][operation_type + ' commissions']
                )
            )


class TestFetchExercisesCase00(TestFetchPositions):
    """Test the fetch_exercises() task of the Accumulator."""

    volume = 100
    operations = [EXERCISE_OPERATION2]
    exercises = {
        OPTION1.symbol: {
            'quantity': 100,
            'price': 1,
            'volume': 0,
        }
    }


class TestFetchExercisesCase01(TestFetchPositions):
    """Test the fetch_exercises() task of the Accumulator."""

    volume = 400
    operations = [EXERCISE_OPERATION2, EXERCISE_OPERATION3]
    exercises = {
        OPTION1.symbol: {
            'quantity': 200,
            'price': 2,
            'volume': 0,
        }
    }
