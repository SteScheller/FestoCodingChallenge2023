from typing import Optional, List

import pytest

import chapter1.puzzle3 as puzzle3


@pytest.mark.parametrize(
    "config, id_, flasks_left, flasks_right",
    [
        ("1 2 3 - 42 0 8 15", None, [1, 2, 3], [42, 0, 8, 15]),
        ("     13: 47 11 - 7", 13, [47, 11], [7]),
    ],
)
def test_parse_config(
    config: str, id_: Optional[bool], flasks_left: List[int], flasks_right: List[int]
):
    assert puzzle3.parse_config(config) == (id_, flasks_left, flasks_right)


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
    "config, result",
    [
        ("4 20 - 5 10", False),
        ("2 - 3 6", True),
        ("2 99999999999999999999999999999999999 - 3 6", True),
        ("4 4 - 3 6", True),
        ("2 4 20 - 2 5 10", True),
    ],
)
def test_is_activated(config: str, result: bool):
    _, left, right = puzzle3.parse_config(config)
    assert puzzle3.is_activated(left, right) == result
