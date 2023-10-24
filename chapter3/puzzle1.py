from typing import List, Tuple, Iterable
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
    if key == "A":
        return True
    elif len(key) == 0:
        return False
    else:
        possible_steps = find_possible_steps(hammers, key)
        for s in possible_steps:
            if is_forgeable(hammers, apply_step(hammers, s, key)):
                return True
    return False


def split_into_segments(key: str) -> List[str]:
    i = 0
    segments = list()
    while i < len(key):
        if key[i : i + 2] == "FE":
            i += 2
            segments.append("FE")
        elif key[i] == "F":
            i += 1
            segments.append("F")
        else:
            j = i + 1
            segment = key[i]
            for j in range(i + 1, len(key)):
                if key[j] == "F":
                    break
                else:
                    segment += key[j]
                    j += 1
            segments.append(segment)
            i = j
    return segments


def shorten_key(hammers: Hammers, key: str) -> Iterable:
    segments = [s if s != "FE" else "C" for s in split_into_segments(key)]
    return "".join(segments)


@cache
def is_long_key_forgeable(hammers: Hammers, key: str) -> bool:
    return is_forgeable(hammers, shorten_key(hammers, key))
