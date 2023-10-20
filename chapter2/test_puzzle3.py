from typing import Optional

import pytest

import chapter2.puzzle3 as puzzle3


@pytest.mark.parametrize(
    "config, id_, flasks",
    [
        ("5 30 310 - X X X", None, (5, 30, 310)),
        ("   60: 2 40 - X X", 60, (2, 40)),
    ],
)
def test_parse_config(config: str, id_: Optional[bool], flasks: puzzle3.Flasks):
    assert puzzle3.parse_config(config)[:2] == (id_, flasks)


@pytest.mark.parametrize(
    "config, result",
    [
        ("4 20 - 5 10", True),
        ("2 - 3 6", False),
        ("2 99999999999999999999999999999999999 - 3 6", True),
        ("4 4 - 3 6", True),
        ("2 4 20 - 2 5 10", True),
    ],
)
def test_fullfils_number_equality(config: str, result: bool):
    _, left, right = puzzle3.parse_config(config)
    assert puzzle3.fullfils_number_equality(left, right) == result


@pytest.mark.parametrize(
    "config, result",
    [
        ("4 20 - 5 10", True),
        ("2 - 3 6", True),
        ("2 99999999999999999999999999999999999 - 3 6", False),
        ("4 4 - 3 6", True),
        ("2 4 20 - 2 5 10", True),
    ],
)
def test_fullfils_weight_equality(config: str, result: bool):
    _, left, right = puzzle3.parse_config(config)
    assert puzzle3.fullfils_weight_equality(left, right) == result


@pytest.mark.parametrize(
    "config, result",
    [
        ("4 20 - 5 10", True),
        ("2 - 3 6", True),
        ("2 99999999999999999999999999999999999 - 3 6", True),
        ("4 4 - 3 6", False),
        ("2 4 20 - 2 5 10", False),
    ],
)
def test_fullfils_diversity(config: str, result: bool):
    _, left, right = puzzle3.parse_config(config)
    assert puzzle3.fullfils_diversity(left, right) == result


@pytest.mark.parametrize(
    "target, current, n, result",
    [
        ((1,), tuple(), 2, False),
        ((1, 2), tuple(), 1, True),
        ((47, 1), tuple(), 1, True),
        ((1, 100), tuple(), 2, False),
        ((2, 100), tuple(), 3, True),
        ((2, 3), (1,), 2, False),
        ((3, 105), (5,), 7, True),
    ],
)
def test_can_total_weight_still_be_reached(
    target: puzzle3.Flasks, current: puzzle3.Flasks, n: int, result: bool
) -> bool:
    assert puzzle3.can_total_weight_still_be_reached(target, current, n) == result


@pytest.mark.parametrize(
    "config, result",
    [
        ("2 6 210 - X X X", False),
        ("2 5 190 - X X X", False),
        ("3 54 - X X", False),
        ("2 7 70 - X X X", False),
        ("8 14 - X X", False),
        ("2 3 33 - X X X", False),
        ("42 1337 - X X", False),
        ("3 105 - X X", True),
        ("5 30 310 - X X X", True),
        ("3 12 - X X", True),
        ("35 6090 - X X", True),
        ("2 30 - X X", True),
        ("5 195 - X X", True),
    ],
)
def test_can_be_balanced(config: str, result: bool):
    _, flasks, _ = puzzle3.parse_config(config)
    assert puzzle3.can_be_balanced(flasks, tuple()) == result
