from chapter1.puzzle1 import create_hammers, Segment, forge_key

HAMMER_COLLECTION = """\
1. A -> BC
2. A -> CB
3. B -> DD
4. B -> BD
5. C -> CD
6. C -> FE
7. D -> AF
8. D -> FA
"""


def test_create_hammers():
    hammers = create_hammers(HAMMER_COLLECTION.splitlines())
    assert len(hammers) == 8
    assert hammers[0].utilize(Segment.A) == [Segment.B, Segment.C]
    assert hammers[1].utilize(Segment.A) == [Segment.C, Segment.B]
    assert hammers[2].utilize(Segment.B) == [Segment.D, Segment.D]
    assert hammers[3].utilize(Segment.B) == [Segment.B, Segment.D]
    assert hammers[4].utilize(Segment.C) == [Segment.C, Segment.D]
    assert hammers[5].utilize(Segment.C) == [Segment.F, Segment.E]
    assert hammers[6].utilize(Segment.D) == [Segment.A, Segment.F]
    assert hammers[7].utilize(Segment.D) == [Segment.F, Segment.A]


def test_forge_key():
    hammers = create_hammers(HAMMER_COLLECTION.splitlines())
    recipe = "(1, 1) - (3, 1) - (7, 2)"
    assert forge_key(hammers, recipe) == "DAFC"
