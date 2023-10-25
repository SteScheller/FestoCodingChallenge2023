from typing import Optional, List, Tuple

import pytest

from chapter3.puzzle3 import (
    Flasks,
    Fraction,
    parse_config,
    compute_water_fractions,
    compute_weight_fraction,
    can_be_balanced,
)


@pytest.mark.parametrize(
    "config, id_, fixed_flasks, free_flasks",
    [
        ("2 - (6)", None, (2,), (6,)),
        ("6 - (2) (3)", None, (6,), (2, 3)),
        ("  60: 2 9 396 - (29) (46) (52)", 60, (2, 9, 396), (29, 46, 52)),
        ("  61: 3 24 - (14) (17)", 61, (3, 24), (14, 17)),
        ("  62: 5 25 850 - (35) (97) (1802)", 62, (5, 25, 850), (35, 97, 1802)),
        ("  63: 4 27 2160 - (356) (632) (1424)", 63, (4, 27, 2160), (356, 632, 1424)),
    ],
)
def test_parse_config(config: str, id_: Optional[bool], fixed_flasks: Flasks, free_flasks: Flasks):
    assert parse_config(config) == (id_, fixed_flasks, free_flasks)


@pytest.mark.parametrize(
    "flasks, fraction_values",
    [
        ((2, 3), {(1, 2), (1, 3), (1, 6)}),
    ],
)
def test_compute_water_fractions(flasks: Flasks, fraction_values: List[Tuple[int, int]]):
    fractions = {Fraction(n, d) for (n, d) in fraction_values}
    assert compute_water_fractions(flasks) == fractions


@pytest.mark.parametrize(
    "flasks, fraction_values",
    [
        ((2, 3), (5, 6)),
        ((1, 2, 3), (11, 6)),
        ((2, 1000000), (500001, 1000000)),
    ],
)
def test_compute_weight_fraction(flasks: Flasks, fraction_values: List[Tuple[int, int]]):
    assert compute_weight_fraction(flasks) == Fraction(*fraction_values)


@pytest.mark.parametrize(
    "config, result",
    [
        ("2 - (6)", True),
        ("6 - (2) (3)", True),
    ],
)
def test_can_be_balanced(config: str, result: bool):
    _, fixed, free = parse_config(config)
    assert can_be_balanced(fixed, free) == result
