from typing import Optional

import pytest

import chapter3.puzzle3 as puzzle3


@pytest.mark.parametrize(
    "config, id_, fixed_flasks, free_flasks",
    [
        ("2 - (6)", None, (2,), (6,)),
        ("6 - (2) (3)", None, (6,), (2, 3)),
        ("  60: 2 9 396 - (29) (46) (52)", 60, (2, 9, 396), (29, 46, 52)),
        ("  61: 3 24 - (14) (17)", 61, (3, 24), (14, 17)),
        ("  62: 5 25 850 - (35) (97) (1802)", 62, (5, 25, 850), (35, 97, 1802)),
        ("  63: 4 27 2160 - (356) (632) (1424)", 63, (4, 27, 2160), (356, 632, 1424)),
    ],
)
def test_parse_config(
    config: str, id_: Optional[bool], fixed_flasks: puzzle3.Flasks, free_flasks: puzzle3.Flasks
):
    assert puzzle3.parse_config(config) == (id_, fixed_flasks, free_flasks)


# @pytest.mark.parametrize(
#     "config, result",
#     [
#         ("2 - (6)", True),
#         ("6 - (2) (3)", True),
#     ],
# )
# def test_can_be_balanced(config: str, result: bool):
#     _, flasks, _ = puzzle3.parse_config(config)
#     assert puzzle3.can_be_balanced(flasks, tuple()) == result
