from typing import Tuple, Optional, Set, Iterable
from re import search
from math import ceil
from itertools import combinations
from fractions import Fraction
from random import shuffle

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

    for x, y in combinations(fractions, 2):
        (bigger, smaller) = (x, y) if x > y else (y, x)
        # the smaller container can be poured into the bigger one multiple times until it is full
        # and some remainder is left
        remainder = ceil(bigger / smaller) * smaller - bigger
        if remainder > 0:  # we don't want to add 0
            fractions.add(remainder)

        # when pouring the bigger container into the smaller the remainder will always be a
        # multiple of the smaller plus some remainder
        remainder = bigger % smaller
        if remainder > 0:  # we don't want to add 0
            fractions.add(remainder)

    return fractions


def compute_weight_fraction(flasks: Flasks) -> Fraction:
    return sum([Fraction(1, n) for n in flasks])


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

    return tuple(sorted(set(filtered)))


def get_int_factor(fractions: Iterable[Fraction]) -> int:
    """Random search a mininmal factor that converts all fractions to integers"""
    min_int_factor = None
    sequence = list(fractions)
    for _ in range(100):
        int_factor = 1
        shuffle(sequence)
        for x in sequence:
            if (x * int_factor).denominator != 1:
                int_factor *= x.denominator
        if min_int_factor is None:
            min_int_factor = int_factor
        else:
            min_int_factor = min(min_int_factor, int_factor)

    return min_int_factor


def compute_coin_change_num(coins: Tuple[int], target: int) -> int:
    # create the ways array
    ways = [0 for _ in range(target + 1)]

    # set the first way to 1 because its 0 and there is 1 way to make 0 with 0 coins
    ways[0] = 1

    # go through all of the coins
    for coin in coins:
        # make a comparison to each index value of ways with the coin value.
        for j in range(len(ways)):
            if coin <= j:
                # update the ways array
                ways[j] += ways[j - coin]

    # return the value at the Nth position of the ways array.
    return ways[target]


def is_divisible_by_any(n: int, numbers: Iterable[int]) -> bool:
    for x in numbers:
        if n % x == 0:
            return True
    return False


def combination_can_be_found(target: Fraction, water_fractions: Tuple[Fraction]) -> bool:
    filtered_water_fractions = filter_fractions(target, water_fractions)
    factor = get_int_factor([target] + list(filtered_water_fractions))
    target_int = int(target * factor)
    water_ints = tuple(int(x * factor) for x in water_fractions)

    result = False
    if len(filtered_water_fractions) == 0:
        result = False
    elif is_divisible_by_any(target_int, water_ints):
        result = True
    else:
        result = compute_coin_change_num(water_ints, target_int) > 0

    # print(f"{len(water_ints)=} {target_int=} {target=} {factor=}")
    # print(f"{[(item.numerator,  item.denominator) for item in filtered_water_fractions]}")
    # print(f"{result=}")

    return result


def can_be_balanced(fixed: Flasks, free: Flasks) -> bool:
    target = compute_weight_fraction(fixed)
    water_fractions = compute_water_fractions(free)
    return combination_can_be_found(target, water_fractions)


# result with this code is 24268 -> wrong :(
# sum(range(1874 + 1)) = 1756875


def compute_per_config_job(config: str) -> int:
    id_, left, right = parse_config(config)
    if can_be_balanced(left, right):
        return id_
    else:
        return 0
