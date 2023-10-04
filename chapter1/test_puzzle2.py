import chapter1.puzzle2 as puzzle2


def test_abc_G():
    g_ops = [
        ("XXXXXXXX; XXXXXXXX; G; Q;", "0"),
        ("XXXXXXXY; XXXXXXXX; G; Q;", "1"),
        ("XXXXXXXY; XXXXXXXY; G; Q;", "10"),
        ("XXXXXXYX; XXXXXXXY; G; Q;", "11"),
        ("XXXXXYXY; XXXXXXYY; G; Q;", "1000"),
    ]

    for task, result in g_ops:
        assert puzzle2.compute_task(task) == result


def test_abc_L():
    l_ops = [
        ("XXXXXXXX; XXXXXXXX; L; Q;", "0"),
        ("XXXXXXXY; XXXXXXXY; L; Q;", "0"),
        ("XXXXXXYX; XXXXXXXY; L; Q;", "1"),
        ("XXXXXXYY; XXXXXXXY; L; Q;", "10"),
        ("XXXXYXXX; XXXXXXXY; L; Q;", "111"),
    ]

    for task, result in l_ops:
        assert puzzle2.compute_task(task) == result
