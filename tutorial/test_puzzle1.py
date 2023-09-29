import tutorial.puzzle1 as puzzle1


def test_is_ordered_key_ordered():
    ordered = [
        "b",
        "cdef",
        "bddf",
        "aaabcccccfff",
    ]

    for k in ordered:
        assert puzzle1.is_ordered_key(k)


def test_is_ordered_key_not_ordered():
    unordered = [
        "ba",
        "acda",
        "afcdeff",
        "aaaaabdfdeef",
    ]

    for k in unordered:
        assert puzzle1.is_ordered_key(k) is False
