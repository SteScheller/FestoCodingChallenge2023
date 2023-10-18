from typing import Tuple, Optional
from functools import reduce
from operator import mul
from math import gcd
from re import search
from itertools import count
from functools import cache

Flasks = Tuple[int]


def get_flasks(input_: str) -> Flasks:
    return tuple(int(x) for x in input_.split(" ") if x != "X")


def parse_config(config: str) -> Tuple[Optional[int], Flasks]:
    m = search(r"(\d+: )?([\d ]+) - ([\d X]+)", config)
    id_, l, r = m.groups()
    if id_ is not None:
        id_ = int(id_[:-2])
    return id_, get_flasks(l), get_flasks(r)


@cache
def compute_weight_fraction(flasks: Flasks) -> Tuple[int, int]:
    if len(flasks) == 0:
        nom = 0
        denom = 0
        divisor = 1
    elif len(flasks) == 1:
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


def can_total_weight_still_be_reached(target: Flasks, current: Flasks, n: int) -> bool:
    n1, d1 = compute_weight_fraction(target)
    n2, d2 = compute_weight_fraction(current)
    if (n2 * d2) == 0:
        return (n * n1) <= ((len(target) - len(current)) * d1)
    elif (n2 / d2) > (n1 / d1):
        return False
    else:
        return (n * (n1 * d2 - n2 * d1)) <= ((len(target) - len(current)) * d1 * d2)


def fullfils_number_equality(left: Flasks, right: Flasks) -> bool:
    return len(left) == len(right)


def fullfils_weight_equality(left: Flasks, right: Flasks) -> bool:
    return compute_weight_fraction(tuple(left)) == compute_weight_fraction(tuple(right))


def fullfils_diversity(left: Flasks, right: Flasks) -> bool:
    lr = list(left) + list(right)
    return len(set(lr)) == len(lr)


def is_balanced(left: Flasks, right: Flasks) -> bool:
    return (
        fullfils_number_equality(left, right)
        and fullfils_diversity(left, right)
        and fullfils_weight_equality(left, right)
    )


@cache
def can_be_balanced(left: Flasks, right: Flasks) -> bool:
    if is_balanced(left, right):
        return True

    for n in count(1):
        if fullfils_number_equality(left, right):
            break

        if not can_total_weight_still_be_reached(left, right, n):
            break

        if n in (right + left):
            continue

        if can_be_balanced(left, right + (n,)):
            return True

    return False
