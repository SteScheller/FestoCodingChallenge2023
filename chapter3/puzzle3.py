from typing import Tuple, Optional, Set, Iterable
from re import search
from operator import mul
from math import gcd
from itertools import permutations, combinations
from functools import reduce
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
        temp = y
        while temp < x:
            temp += y
        remaining = temp - x
        if remaining > 0:
            fractions.add(remaining)

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


def get_int_factor(target: Fraction, fractions: Iterable[Fraction]) -> int:
    int_factor = target.denominator
    for f in fractions:
        temp = f * int_factor
        int_factor *= temp.denominator

    return int_factor


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
    factor = get_int_factor(target, filtered_water_fractions)
    target_int = int(target * factor)
    water_ints = tuple(int(x * factor) for x in water_fractions)

    # print(f"{len(water_ints)=} {target_int=}")

    result = False
    if len(filtered_water_fractions) == 0:
        result = False
    elif is_divisible_by_any(target_int, water_ints):
        result = True
    else:
        result = compute_coin_change_num(water_ints, target_int) > 0

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
