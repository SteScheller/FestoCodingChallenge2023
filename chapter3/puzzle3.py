from typing import Tuple, Optional
from re import search

Flasks = Tuple[int]


def get_fixed_flasks(input_: str) -> Flasks:
    return tuple(int(x) for x in input_.split(" ") if x != "X")


def get_free_flasks(input_: str) -> Flasks:
    return tuple(int(x[1:-1]) for x in input_.split(" ") if x != "X")


def parse_config(config: str) -> Tuple[Optional[int], Flasks]:
    m = search(r"(\d+: )?([\d ]+) - ((\(\d+\) ?)+)", config)
    id_, l, r, _ = m.groups()
    if id_ is not None:
        id_ = int(id_[:-2])
    return id_, get_fixed_flasks(l), get_free_flasks(r)


def can_be_balanced(left: Flasks, right: Flasks) -> bool:
    return False
