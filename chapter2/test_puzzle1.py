from typing import List

import pytest

from chapter2.puzzle1 import Hammer, create_hammers, is_forgeable


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
        ("DD", True),
        ("BD", True),
        ("CD", True),
        ("FE", True),
        ("AF", True),
        ("FA", True),
        ("EE", False),
    ],
)
def test_is_forgable(hammers: List[Hammer], key: str, is_forgeable_result: bool):
    assert is_forgeable(hammers, key) == is_forgeable_result
