from typing import List, Tuple

import pytest

from chapter1.puzzle1 import create_hammers, Hammer, Segment, forge_key


@pytest.fixture(scope="module")
def hammers() -> List[Hammer]:
    hammer_collection = (
        "1. A -> BC",
        "2. A -> CB",
        "3. B -> DD",
        "4. B -> BD",
        "5. C -> CD",
        "6. C -> FE",
        "7. D -> AF",
        "8. D -> FA",
    )
    yield create_hammers(hammer_collection)


def test_create_hammers(hammers: List[Hammer]):
    assert len(hammers) == 8


@pytest.mark.parametrize(
    "hammer_index, input_segment, output_segments",
    [
        (0, Segment.A, [Segment.B, Segment.C]),
        (1, Segment.A, [Segment.C, Segment.B]),
        (2, Segment.B, [Segment.D, Segment.D]),
        (3, Segment.B, [Segment.B, Segment.D]),
        (4, Segment.C, [Segment.C, Segment.D]),
        (5, Segment.C, [Segment.F, Segment.E]),
        (6, Segment.D, [Segment.A, Segment.F]),
        (7, Segment.D, [Segment.F, Segment.A]),
    ],
)
def test_hammer_utilize(
    hammers: List[Hammer],
    hammer_index: int,
    input_segment: Segment,
    output_segments: Tuple[Segment, Segment],
):
    assert hammers[hammer_index].utilize(input_segment) == output_segments


def test_forge_key(hammers: List[Hammer]):
    recipe = "(1, 1) - (3, 1) - (7, 2)"
    assert forge_key(hammers, recipe) == "DAFC"
