import pytest

import chapter1.puzzle2 as puzzle2


@pytest.mark.parametrize(
    "task, result",
    [
        ("XXXXXXXX; XXXXXXXX; G; Q;", "0"),
        ("XXXXXXXY; XXXXXXXX; G; Q;", "1"),
        ("XXXXXXXY; XXXXXXXY; G; Q;", "10"),
        ("XXXXXXYX; XXXXXXXY; G; Q;", "11"),
        ("XXXXXYXY; XXXXXXYY; G; Q;", "1000"),
        ("XXXXXXXX; XXXXXXXX; L; Q;", "0"),
        ("XXXXXXXY; XXXXXXXY; L; Q;", "0"),
        ("XXXXXXYX; XXXXXXXY; L; Q;", "1"),
        ("XXXXXXYY; XXXXXXXY; L; Q;", "10"),
        ("XXXXYXXX; XXXXXXXY; L; Q;", "111"),
    ],
)
def test_compute_task(task: str, result: str):
    assert puzzle2.compute_task(task) == result
