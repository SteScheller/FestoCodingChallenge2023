from typing import Tuple, Optional, Set
from re import search
from math import gcd
from operator import mul
from itertools import permutations
from functools import reduce, cache
from copy import deepcopy
from fractions import Fraction

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


def compute_water_fractions(flasks: Flasks) -> Set[Fraction]:
    fractions = {Fraction(1, n) for n in flasks}

    for x, y in permutations(fractions, 2):
        temp = deepcopy(y)
        while temp <= x:
            fractions.add(temp)
            temp += y
        fractions.add(temp - x)

    return fractions


@cache
def compute_weight_fraction(flasks: Flasks) -> Fraction:
    if len(flasks) == 0:
        nom = 0
        denom = 0
    elif len(flasks) == 1:
        nom = 1
        denom = flasks[0]
    else:
        summands = list()
        for i in range(len(flasks)):
            x, y = flasks[:i], flasks[i + 1 :]
            factor = reduce(mul, x + y)
            summands.append(factor)
        nom = sum(summands)
        denom = reduce(mul, flasks)
    return Fraction(nom, denom)


def is_linear_combination(target: Fraction, free: Fraction) -> bool:
    selectors = list()
    denominators = list(set([x.denominator for x in free]))

    for i in range(1, 2 ** len(denominators)):
        selectors.append([bool(i & (1 << x)) for x in range(len(denominators))])

    for sel in selectors:
        factors = [x for i, x in enumerate(denominators) if sel[i]]
        temp = reduce(mul, factors)
        c = gcd(target.denominator, temp)
        if target.denominator == c:
            return True

    return False


def can_be_balanced(fixed: Flasks, free: Flasks) -> bool:
    target = compute_weight_fraction(fixed)
    water_fractions = compute_water_fractions(free)
    return is_linear_combination(target, water_fractions)
