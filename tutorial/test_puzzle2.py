import pytest

import tutorial.puzzle2 as puzzle2


@pytest.mark.parametrize(
    "task, result",
    [
        ("X; X; R; Q;", "0"),
        ("X; Y; R; Q;", "1"),
        ("Y; X; R; Q;", "1"),
        ("Y; Y; R; Q;", "1"),
        ("X; X; N; Q;", "0"),
        ("Y; X; N; Q;", "0"),
        ("X; Y; N; Q;", "0"),
        ("Y; Y; N; Q;", "1"),
    ],
)
def test_compute_task(task: str, result: str):
    assert puzzle2.compute_task(task) == result
