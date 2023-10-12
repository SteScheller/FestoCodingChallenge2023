from typing import List, Tuple
from re import search
from functools import cache


class Hammer:
    def __init__(self, transformation: str) -> None:
        m = search(r"([A-F]) -> ([A-F]+)", transformation)
        if m is not None:
            self.input_segment = m.group(1)
            self.output_segments = m.group(2)
        else:
            self.input_segment = None
            self.output_segments = list()


Hammers = Tuple[Hammer]


def create_hammers(hammer_collection: List[str]) -> Hammers:
    return tuple([Hammer(h) for h in hammer_collection])


Step = Tuple[int, int]


def find_possible_steps(hammers: Hammers, key: str) -> List[Step]:
    steps = list()
    for hammer_idx, h in enumerate(hammers):
        for key_idx in range(len(key) - 1):
            if key[key_idx : key_idx + 2] == h.output_segments:
                steps.append((hammer_idx, key_idx))
    return steps


def apply_step(hammers: Hammers, step: Step, key: str) -> str:
    hammer_idx, key_idx = step
    return key[:key_idx] + hammers[hammer_idx].input_segment + key[key_idx + 2 :]


@cache
def is_forgeable(hammers: Hammers, key: str) -> bool:
    if len(key) == 0:
        return False
    if len(key) == 1:
        return key == "A"
    else:
        possible_steps = find_possible_steps(hammers, key)
        for s in possible_steps:
            if is_forgeable(hammers, apply_step(hammers, s, key)):
                return True
    return False
