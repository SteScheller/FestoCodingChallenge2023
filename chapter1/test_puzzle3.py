import chapter1.puzzle3 as puzzle3


def test_parse_config():
    assert (None, [1, 2, 3], [42, 0, 8, 15]) == puzzle3.parse_config("1 2 3 - 42 0 8 15")
    assert (13, [47, 11], [7]) == puzzle3.parse_config("     13: 47 11 - 7")


def test_fullfils_number_equality():
    test_data = [
        ("4 20 - 5 10", True),
        ("2 - 3 6", False),
        ("2 99999999999999999999999999999999999 - 3 6", True),
        ("4 4 - 3 6", True),
        ("2 4 20 - 2 5 10", True),
    ]
    for config, result in test_data:
        _, left, right = puzzle3.parse_config(config)
        assert puzzle3.fullfils_number_equality(left, right) == result


def test_fullfils_weight_equality():
    test_data = [
        ("4 20 - 5 10", True),
        ("2 - 3 6", True),
        ("2 99999999999999999999999999999999999 - 3 6", False),
        ("4 4 - 3 6", True),
        ("2 4 20 - 2 5 10", True),
    ]
    for config, result in test_data:
        _, left, right = puzzle3.parse_config(config)
        assert puzzle3.fullfils_weight_equality(left, right) == result


def test_fullfils_diversity():
    test_data = [
        ("4 20 - 5 10", True),
        ("2 - 3 6", True),
        ("2 99999999999999999999999999999999999 - 3 6", True),
        ("4 4 - 3 6", False),
        ("2 4 20 - 2 5 10", False),
    ]
    for config, result in test_data:
        _, left, right = puzzle3.parse_config(config)
        assert puzzle3.fullfils_diversity(left, right) == result


def test_is_activated():
    test_data = [
        ("4 20 - 5 10", False),
        ("2 - 3 6", True),
        ("2 99999999999999999999999999999999999 - 3 6", True),
        ("4 4 - 3 6", True),
        ("2 4 20 - 2 5 10", True),
    ]
    for config, result in test_data:
        _, left, right = puzzle3.parse_config(config)
        assert puzzle3.is_activated(left, right) == result
