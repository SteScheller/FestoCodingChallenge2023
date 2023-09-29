import tutorial.puzzle2 as puzzle2


def test_abc_R():
    r_ops = [
        ("X; X; R; Q;", "0"),
        ("X; Y; R; Q;", "1"),
        ("Y; X; R; Q;", "1"),
        ("Y; Y; R; Q;", "1"),
    ]

    for task, result in r_ops:
        assert puzzle2.compute_task(task) == result


def test_abc_N():
    q_ops = [
        ("X; X; N; Q;", "0"),
        ("Y; X; N; Q;", "0"),
        ("X; Y; N; Q;", "0"),
        ("Y; Y; N; Q;", "1"),
    ]

    for task, result in q_ops:
        assert puzzle2.compute_task(task) == result
