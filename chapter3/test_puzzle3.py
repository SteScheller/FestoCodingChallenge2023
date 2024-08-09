from typing import Optional, List, Tuple, Set, Iterable

import pytest

from chapter3.puzzle3 import (
    Flasks,
    Fraction,
    parse_config,
    compute_water_fractions,
    filter_fractions,
    compute_weight_fraction,
    can_be_balanced,
    get_int_factor,
)


@pytest.mark.parametrize(
    "config, id_, fixed_flasks, free_flasks",
    [
        ("2 - (6)", None, (2,), (6,)),
        ("6 - (2) (3)", None, (6,), (2, 3)),
        ("4 9 - (1) (2) (36)", None, (4, 9), (1, 2, 36)),
        ("4 9 - (3) (12)", None, (4, 9), (3, 12)),
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
        ((3, 12), {(1, 3), (1, 12)}),
        ((2, 7), {(1, 2), (1, 7), (1, 14)}),
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
        ((4, 9), (13, 36)),
    ],
)
def test_compute_weight_fraction(flasks: Flasks, fraction_values: List[Tuple[int, int]]):
    assert compute_weight_fraction(flasks) == Fraction(*fraction_values)


@pytest.mark.parametrize(
    "fraction_values, target_values, filtered_fraction_values",
    [
        ({(1, 3), (1, 2), (1, 4)}, (8, 12), ((1, 4), (1, 3))),
        ({(1, 3), (1, 12), (1, 4)}, (1, 4), ((1, 12),)),
        ({(1, 2), (1, 7), (1, 14), (3, 14), (5, 14)}, (4, 15), ((1, 14),)),
    ],
)
def test_filter_fractions(
    fraction_values: Set[Tuple[int, int]],
    target_values: Tuple[int, int],
    filtered_fraction_values: Tuple[Tuple[int, int]],
):
    fractions = {Fraction(n, d) for (n, d) in fraction_values}
    filtered_fractions = tuple(Fraction(n, d) for (n, d) in filtered_fraction_values)
    assert filter_fractions(Fraction(*target_values), fractions) == filtered_fractions


@pytest.mark.parametrize(
    "config, result",
    [
        ("2 - (6)", True),
        ("6 - (2) (3)", True),
        ("3 - (1) (2) (4)", False),
        ("4 9 - (1) (2) (36)", True),
        ("4 9 - (3) (12)", False),
        ("3 9 - (18) (36)", True),
    ],
)
def test_can_be_balanced(config: str, result: bool):
    _, fixed, free = parse_config(config)
    assert can_be_balanced(fixed, free) == result


@pytest.mark.parametrize(
    "fractions, expected",
    [
        ((Fraction(1, 8), Fraction(1, 3), Fraction(1, 2)), 24),
        ((Fraction(1, 4), Fraction(1, 2), Fraction(1, 8)), 8),
        ((Fraction(1, 8), Fraction(1, 2), Fraction(1, 4)), 8),
        ((Fraction(1, 2), Fraction(1, 8), Fraction(1, 4)), 8),
        ((Fraction(1, 3), Fraction(1, 5), Fraction(1, 7)), 105),
    ],
)
def test_get_int_factor(fractions: Iterable[Fraction], expected: int):
    assert get_int_factor(fractions) == expected
