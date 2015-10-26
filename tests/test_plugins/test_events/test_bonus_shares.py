"""Tests for BonusShares events."""

from __future__ import absolute_import

from tests.fixtures.events import EVENT6, EVENT7, EVENT8
from tests.fixtures.logs import (
    LogTest,
)
from tests.fixtures.accumulator_states import (
    INITIAL_STATE0, EXPECTED_STATE0, EXPECTED_STATE21,
    EXPECTED_STATE22
)


class TestBonusSharesCase00(LogTest):
    """Test a bonus shares event with factor 1."""

    initial_state = INITIAL_STATE0
    occurrences = [EVENT6]
    expected_state = EXPECTED_STATE0


class TestBonusSharesCase01(LogTest):
    """Test a bonus shares event with factor 2."""

    initial_state = INITIAL_STATE0
    occurrences = [EVENT8]
    expected_state = EXPECTED_STATE21


class TestBonusSharesCase02(LogTest):
    """Test a bonus shares event with factor 0.5."""

    initial_state = INITIAL_STATE0
    occurrences = [EVENT7]
    expected_state = EXPECTED_STATE22
