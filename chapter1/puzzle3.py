from typing import List, Tuple, Optional
from functools import reduce
from operator import mul
from math import gcd
from re import search

Flasks = List[int]


def get_flasks(input_: str) -> Flasks:
    return [int(x) for x in input_.split(" ")]


def parse_config(config: str) -> Tuple[Optional[int], Flasks, Flasks]:
    m = search(r"(\d+: )?([\d ]+) - ([\d ]+)", config)
    id_, l, r = m.groups()
    if id_ is not None:
        id_ = int(id_[:-2])
    return id_, get_flasks(l), get_flasks(r)


def fullfils_number_equality(left: Flasks, right: Flasks) -> bool:
    return len(left) == len(right)


def fullfils_weight_equality(left: Flasks, right: Flasks) -> bool:
    def compute_weight_fraction(flasks: Flasks) -> Tuple[int, int]:
        if len(flasks) == 1:
            nom = 1
            denom = flasks[0]
            divisor = 1
        else:
            summands = list()
            for i in range(len(flasks)):
                x, y = flasks[:i], flasks[i + 1 :]
                factor = reduce(mul, x + y)
                summands.append(factor)
            nom = sum(summands)
            denom = reduce(mul, flasks)
            divisor = gcd(nom, denom)
        return nom // divisor, denom // divisor

    return compute_weight_fraction(left) == compute_weight_fraction(right)


def fullfils_diversity(left: Flasks, right: Flasks) -> bool:
    lr = left + right
    return len(set(lr)) == len(lr)


def is_activated(left: Flasks, right: Flasks) -> bool:
    return not (
        fullfils_number_equality(left, right)
        and fullfils_weight_equality(left, right)
        and fullfils_diversity(left, right)
    )
