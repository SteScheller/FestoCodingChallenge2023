from typing import Optional, List

import pytest

import chapter2.puzzle3 as puzzle3


@pytest.mark.parametrize(
    "config, id_, flasks",
    [
        ("5 30 310 - X X X", None, [5, 30, 310]),
        ("   60: 2 40 - X X", 60, [2, 40]),
    ],
)
def test_parse_config(config: str, id_: Optional[bool], flasks: List[int]):
    assert puzzle3.parse_config(config) == (id_, flasks)


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
    _, flasks = puzzle3.parse_config(config)
    assert puzzle3.can_be_balanced(flasks) == result
