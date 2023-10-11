import pytest

from tutorial.puzzle3 import compute_state, State


@pytest.mark.parametrize(
    "log, result",
    [
        ("idle reversed ready reversed toggled reversed reversed", State.unsafe),
        ("ready inverted switched quiet inverted flipped reversed", State.unsafe),
        ("primed ready switched ready toggled disabled toggled", State.unsafe),
        ("live reversed flipped inverted inverted inverted reversed", State.unsafe),
        ("inactive flipped flipped reversed active live", State.unsafe),
        ("quiet live active inactive armed reversed flipped", State.unsafe),
        ("disabled inverted inverted standby flipped switched inverted", State.unsafe),
        ("live quiet disabled flipped toggled toggled reversed toggled", State.unsafe),
        ("standby toggled inverted reversed reversed switched", State.unsafe),
        ("armed live flipped flipped ready reversed", State.safe),
    ],
)
def test_compute_state(log: str, result: State):
    assert compute_state(log) == result
