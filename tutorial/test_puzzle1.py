import pytest

import tutorial.puzzle1 as puzzle1


@pytest.mark.parametrize(
    "key, result",
    [
        ("b", True),
        ("cdef", True),
        ("bddf", True),
        ("aaabcccccfff", True),
        ("ba", False),
        ("acda", False),
        ("afcdeff", False),
        ("aaaaabdfdeef", False),
    ],
)
def test_is_ordered(key: str, result: bool):
    assert puzzle1.is_ordered_key(key) == result
