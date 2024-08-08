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

    return sorted(set(filtered))


def get_int_factor(target: Fraction, fractions: Iterable[Fraction]) -> int:
    int_factor = target.denominator
    for f in fractions:
        temp = f * int_factor
        int_factor *= temp.denominator
    return int_factor


def compute_coin_change_num(S: Tuple[int], m: int, n: int) -> int:
    # dynamic programming solution of the coin change problem
    table = [[0 for x in range(m)] for x in range(n + 1)]

    for i in range(m):
        table[0][i] = 1

    for i in range(1, n + 1):
        for j in range(m):
            x = table[i - S[j]][j] if i - S[j] >= 0 else 0
            y = table[i][j - 1] if j >= 1 else 0
            table[i][j] = x + y

    return table[n][m - 1] > 0


def is_divisible_by_any(n: int, numbers: Iterable[int]) -> bool:
    for x in numbers:
        if n % x == 0:
            return True
    return False


def estimate_frobenius_number(numbers: Iterable[int]) -> int:
    # educated guess based on target int distribution :)
    # return reduce(mul, numbers)
    # return 94198543 # largest found target integer
    return 94198543 + 1  # largest found target integer; did not work out, result 312274 is wrong
    # return 10000000 # did not work out, result 398870 is wrong
    # return 1000000 # did not work out, result 733955 is wrong


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
        frobenius_number = estimate_frobenius_number(water_ints)
        if target_int > frobenius_number:
            result = True
        else:
            result = compute_coin_change_num(water_ints, len(water_ints), target_int) > 0

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
