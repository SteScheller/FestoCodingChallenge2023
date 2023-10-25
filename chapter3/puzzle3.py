from typing import Tuple, Optional, Set, Iterable
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


@cache
def combination_can_be_found(
    target: Fraction, current: Fraction, used_fractions: Tuple[Fraction]
) -> bool:
    if target == current:
        return True
    elif current > target:
        return False
    else:
        for x in used_fractions:
            if combination_can_be_found(target, current + x, used_fractions):
                return True
    return False


def is_linear_combination(target: Fraction, fractions: Set[Fraction]) -> bool:
    # selectors = list()
    fractions = list(fractions)

    # prepare possible selection of used fractions
    # for i in range(1, 2 ** len(fractions)):
    #    selectors.append([bool(i & (1 << x)) for x in range(len(fractions))])

    # find possibly used fractions by finding combinations whos denominators multiply to a
    # multiple of the denominator of the target fraction
    # candidates = list()
    # denominators = [x.denominator for x in fractions]
    # for sel in selectors:
    #    factors = [x for i, x in enumerate(denominators) if sel[i]]
    #    temp = reduce(mul, factors)
    #    c = gcd(target.denominator, temp)
    #    if target.denominator == c:
    #        candidates.append(sel)

    # check if fractions can be added up to the target fraction
    used_fractions = fractions
    used_fractions.sort(reverse=True)
    return combination_can_be_found(target, Fraction(0, target.denominator), tuple(used_fractions))

    # for sel in candidates:
    #     used_fractions = [x for i, x, in enumerate(fractions) if sel[i]]
    #     used_fractions.sort(reverse=True)
    #     if combination_can_be_found(target, Fraction(0, target.denominator), tuple(used_fractions)):
    #         return True

    # return False


def filter_fractions(fractions: Iterable[Fraction]) -> Tuple[Fraction]:
    fractions = sorted(set(fractions))
    filtered = [fractions[0]]

    for f in fractions[1:]:
        is_multiple = False
        for ff in filtered:
            if ((f // ff) * ff) == f:
                is_multiple = True
                break
        if not is_multiple:
            filtered.append(f)
    return tuple(filtered)


def can_be_balanced(fixed: Flasks, free: Flasks) -> bool:
    target = compute_weight_fraction(fixed)
    water_fractions = compute_water_fractions(free)
    water_fractions = filter_fractions(water_fractions)
    print(target)
    print(water_fractions)
    return combination_can_be_found(target, Fraction(0, target.denominator), water_fractions)
