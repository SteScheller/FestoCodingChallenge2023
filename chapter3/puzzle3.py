from typing import Tuple, Optional, Set
from re import search
from math import gcd
from operator import mul
from itertools import permutations
from functools import total_ordering, reduce, cache
from copy import deepcopy

Flasks = Tuple[int]


@total_ordering
class Fraction:
    def __init__(self, nom, denom):
        c = gcd(nom, denom)
        self.__nom = nom // c
        self.__denom = denom // c

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        c = gcd(value, self.__denom)
        self.__nom = value // c
        self.__denom = self.__denom // c

    @property
    def denom(self):
        return self.__denom

    @denom.setter
    def denom(self, value):
        c = gcd(value, self.__nom)
        self.__nom = self.__nom // c
        self.__denom = value // c

    def __add__(self, other):
        n = self.__nom * other.denom + other.nom * self.__denom
        d = self.__denom * other.denom
        return Fraction(n, d)

    def __sub__(self, other):
        n = self.__nom * other.denom - other.nom * self.__denom
        d = self.__denom * other.denom
        return Fraction(n, d)

    def __eq__(self, other):
        return (self.__nom == other.nom) and (self.__denom == other.denom)

    def __lt__(self, other):
        t = self - other
        return (t.nom * t.denom) <= 0

    def __hash__(self):
        return hash((self.__nom, self.__denom))


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


def can_be_balanced(fixed: Flasks, free: Flasks) -> bool:
    target = compute_weight_fraction(fixed)
    water_fractions = compute_water_fractions(free)
    return target in water_fractions
