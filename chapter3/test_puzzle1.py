from typing import List, Set

import pytest

from chapter3.puzzle1 import (
    create_hammers,
    Hammer,
    Hammers,
    is_forgeable,
    apply_step,
    Step,
    find_possible_steps,
    split_into_segments,
    is_long_key_forgeable,
)


@pytest.fixture(scope="module")
def hammers() -> List[Hammer]:
    hammer_collection = (
        "A -> BC",
        "A -> CB",
        "B -> DD",
        "B -> BD",
        "C -> CD",
        "C -> FE",
        "D -> AF",
        "D -> FA",
    )
    yield create_hammers(hammer_collection)


@pytest.mark.parametrize(
    "key, is_forgeable_result",
    [
        ("BC", True),
        ("CB", True),
        ("DD", False),
        ("BD", False),
        ("CD", False),
        ("FE", False),
        ("AF", False),
        ("FA", False),
        ("EE", False),
        ("EF", False),
        ("AAA", False),
        ("BFE", True),
        ("FEAF", False),
    ],
)
def test_is_forgable(hammers: Hammers, key: str, is_forgeable_result: bool):
    assert is_forgeable(hammers, key) == is_forgeable_result


@pytest.mark.parametrize(
    "step, key, result_key",
    [
        ((7, 0), "FABCD", "DBCD"),
        ((0, 2), "FABCD", "FAAD"),
        ((4, 3), "FABCD", "FABC"),
        ((6, 0), "AFBCBDD", "DBCBDD"),
        ((0, 2), "AFBCBDD", "AFABDD"),
        ((1, 3), "AFBCBDD", "AFBADD"),
        ((3, 4), "AFBCBDD", "AFBCBD"),
        ((2, 5), "AFBCBDD", "AFBCBB"),
    ],
)
def test_apply_step(hammers: Hammers, step: Step, key: str, result_key):
    assert apply_step(hammers, step, key) == result_key


@pytest.mark.parametrize(
    "key, result_steps",
    [
        ("BC", {(0, 0)}),
        ("BCBC", {(0, 0), (0, 2), (1, 1)}),
        ("AFBCBDD", {(6, 0), (0, 2), (1, 3), (3, 4), (2, 5)}),
    ],
)
def test_find_possible_steps(hammers: Hammers, key: str, result_steps: Set[Step]):
    assert set(find_possible_steps(hammers, key)) == result_steps


@pytest.mark.parametrize(
    "key, result_segments",
    [
        ("BC", ["BC"]),
        (
            "FEFAFFEBFFCBFEFFDFBFDCBAFFEFFE",
            [
                "FE",
                "F",
                "A",
                "F",
                "FE",
                "B",
                "F",
                "F",
                "CB",
                "FE",
                "F",
                "F",
                "D",
                "F",
                "B",
                "F",
                "DCBA",
                "F",
                "FE",
                "F",
                "FE",
            ],
        ),
        (
            "FEFDDFEFFEFADFFEADCDFFBFE",
            ["FE", "F", "DD", "FE", "F", "FE", "F", "AD", "F", "FE", "ADCD", "F", "F", "B", "FE"],
        ),
    ],
)
def test_split_into_segments(key: str, result_segments: List[str]):
    assert split_into_segments(key) == result_segments


@pytest.mark.parametrize(
    "key, is_forgeable_result",
    [
        ("BC", True),
        ("CB", True),
        ("DD", False),
        ("BD", False),
        ("CD", False),
        ("FE", False),
        ("AF", False),
        ("FA", False),
        ("EE", False),
        ("EF", False),
        ("AAA", False),
        ("BFE", True),
        ("FEAF", False),
        ("CFCDDFBFED", True),
        ("AFBFACDDFFE", True),
        ("CDAFDFAFA", True),
        ("CDFDDCCBF", True),
        ("FEDAFFCBB", True),
        ("CCDDFFCDD", True),
        ("CDAFCBFFA", True),
        ("FEFFEBFBDCBDFCFBC", True),
        ("AFFCBCDBFBCDFFEFA", True),
        ("FEDDFEFFFEDBDCFFA", True),
        ("FCFABDFFEDFABFEFC", True),
        ("FBDCFAFFEBDCDBDCF", True),
        ("FEFCDBDAFFAFAFFEDCBFFFEFCDDDFCBAF", True),
        ("BCFDFEFFEAFDDBDAFFEAFDFFBCCBFFEDF", True),
        ("FEFEFEBDDCFFFAFAFFEFFBCFEDDFFEBDF", True),
        ("FACBFBDCFCBFFBDFEBFEDFFEFBFEFFAFE", True),
        ("FEAFBDFEFFABCDDFFADCAFDFAFFEAFFAF", True),
    ],
)
def test_is_long_key_forgable(hammers: Hammers, key: str, is_forgeable_result: bool):
    assert is_long_key_forgeable(hammers, key) == is_forgeable_result
