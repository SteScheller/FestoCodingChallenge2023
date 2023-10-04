import re
from enum import Enum
from typing import List, Optional
from copy import copy


class Segment(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"


class Hammer:
    def __init__(self, transformation: str) -> None:
        m = re.search(r"([A-F]) -> ([A-F]+)", transformation)
        if m is not None:
            self.input_segment = Segment(m.group(1))
            self.output_segments = [Segment(s) for s in m.group(2)]
        else:
            self.input_segment = None
            self.output_segments = list()

    def utilize(self, segment: Segment) -> Optional[List[Segment]]:
        if segment == self.input_segment:
            return copy(self.output_segments)
        else:
            return None

    def is_applicable(self, segment: Segment) -> bool:
        return segment == self.input_segment


def create_hammers(hammer_collection: List[str]) -> List[Hammer]:
    return [Hammer(h) for h in hammer_collection]


def forge_key(hammers: List[Hammer], recipe: str) -> Optional[str]:
    key = "A"
    for m in re.finditer(r"\((\d+), (\d+)\)", recipe):
        hammer_idx = int(m.group(1)) - 1
        segment_idx = int(m.group(2)) - 1
        if (
            not (hammer_idx in range(len(hammers)))
            or not (segment_idx in range(len(key)))
            or not (hammers[hammer_idx].is_applicable(Segment(key[segment_idx])))
        ):
            return None
        else:
            new_segments = hammers[hammer_idx].utilize(Segment(key[segment_idx]))
        key = key[:segment_idx] + "".join([s.value for s in new_segments]) + key[segment_idx + 1 :]
    return key
