import pytest

import chapter2.puzzle2 as puzzle2


@pytest.mark.parametrize(
    "task, result",
    [
        ("XXXXXXXX; XXYXXXXX; G; E;", "64"),
        ("XXYXXXXX; XXXXXXXX; L; E;", "16"),
        ("XXXXXXXX; XYXXXXXX; G; E;", "32"),
        ("XXXYXXXX; XXXXXXXX; L; E;", "32"),
        ("XXXYXYXY; XXYXYXYX; W; Q;", "10110010"),
        ("YYXYXXXY; YXYXYXYX; G; E;", "171"),
        ("XYXYYYXX; XYXXYYYY; W; Q;", "11010100"),
        ("XXXYYYYX; YYYYXXXY; L; E;", "61"),
        ("YYXYXYXY; YXYXYXYX; L; Q;", "11011"),
        ("XYYXYYYY; YYXYYYYY; W; E;", "225"),
    ],
)
def test_compute_task(task: str, result: str):
    assert puzzle2.compute_task(task) == result
