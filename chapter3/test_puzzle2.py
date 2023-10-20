import pytest

import chapter3.puzzle2 as puzzle2


@pytest.mark.parametrize(
    "task, result",
    [
        ("XXXXXXYY; XXXXXXYY; P; Q;", "1"),
        ("YXXXXXXX; XXXXYXXX; P; E;", "16"),
        ("XXXXYXYX; XXXXXXXY; P; F;", "a"),
        ("XXXXXYYX; XXXXXYXY; P; F;", "1"),
        ("XXXXYXXX; XXXXXYXY; P; F;", "2"),
        ("XXXXXXYY; XXXXXXYX; P; F;", "2"),
        ("XYXYXXYY; XXXXXXYY; P; E;", "33"),
        ("YXYXXXXX; XXXXYYXX; P; E;", "12"),
        ("XYXYYXYY; XXXXYXYX; P; F;", "b"),
        ("YYXXXXXX; XXXXXXYY; P; F;", "40"),
        ("XXXXXXYX; XXXXXXXY; M; Q;", "1"),
        ("XXXXXXYX; YXXXXXXX; M; E;", "4"),
        ("XXXXXYYX; YXXXXXXX; M; F;", "c"),
        ("XXXYXXXX; YXXXXXXX; M; E;", "64"),
        ("YXXXXXYX; YXXXXXXX; M; Q;", "101"),
        ("YXXYYXYY; XXXXXXXY; M; F;", "d5"),
        ("YXXXYYYY; YXXXXXXX; M; Q;", "11111"),
        ("XXXXXXYY; XXXXXXXY; M; E;", "129"),
        ("YYYXXXXX; YXXXXXXX; M; Q;", "10100001"),
        ("XYXYYXYY; XXXXXXXY; M; F;", "b5"),
    ],
)
def test_compute_task(task: str, result: str):
    assert puzzle2.compute_task(task) == result
