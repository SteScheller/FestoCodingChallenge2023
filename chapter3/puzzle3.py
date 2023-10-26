from typing import Tuple, Optional, Set, Iterable
from re import search
from operator import mul
from math import gcd
from itertools import permutations, combinations
from functools import reduce, cache
from copy import deepcopy
from fractions import Fraction

import sys

sys.setrecursionlimit(30000)

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


def combination_can_be_found(
    target: Fraction, current: Fraction, used_fractions: Tuple[Fraction]
) -> bool:
    if target == current:
        return True
    elif current > target:
        return False
    elif len(used_fractions) == 1:
        return ((target - current) % used_fractions[0]) == 0
    else:
        for i, x in enumerate(used_fractions):
            if ((target - current) % x) == 0:
                return True
            if combination_can_be_found(target, current + x, used_fractions[i:]):
                return True
    return False


def filter_fractions(target: Fraction, fractions: Iterable[Fraction]) -> Tuple[Fraction]:
    fractions = sorted(set(fractions))
    filtered = [fractions[0]]

    # remove fractions that are to big or are multiples of other smaller fractions
    for f in fractions[1:]:
        if f > target:
            break
        is_multiple = False
        for ff in filtered:
            if (f % ff) == 0:
                is_multiple = True
                break
        if not is_multiple:
            filtered.append(f)

    filtered_denominators = set()
    denominators = {x.denominator for x in filtered}
    for n in range(1, len(denominators) + 1):
        for dd in combinations(denominators, n):
            gcd_ = gcd(target.denominator, reduce(mul, dd))
            if gcd_ == target.denominator:
                filtered_denominators.update(dd)
    filtered = [f for f in filtered if f.denominator in filtered_denominators]
    return tuple(reversed(filtered))


def can_be_balanced(fixed: Flasks, free: Flasks) -> bool:
    target = compute_weight_fraction(fixed)
    water_fractions = compute_water_fractions(free)
    water_fractions = filter_fractions(target.denominator, water_fractions)
    return combination_can_be_found(target, Fraction(0, target.denominator), water_fractions)


def compute_per_config_job(config: str) -> int:
    id_, left, right = parse_config(config)
    if can_be_balanced(left, right):
        return id_
    else:
        return 0
