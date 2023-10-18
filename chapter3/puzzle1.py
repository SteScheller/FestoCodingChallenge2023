import multiprocessing as mp
from typing import List

from chapter2.puzzle1 import create_hammers, is_forgeable, Hammers

create_hammers = create_hammers


class CreateHammersJob:
    def __init__(self, hammers: Hammers):
        self.hammers = hammers

    def __call__(self, key: str):
        result = is_forgeable(self.hammers, key)
        print(".", end="")
        return result


def find_forgable_keys(hammers: Hammers, keys: List[str]) -> List[int]:
    print(mp.cpu_count())
    job = CreateHammersJob(hammers)
    with mp.Pool(mp.cpu_count()) as p:
        forgeable = p.map(job, keys)

    keys = [k for k, f in zip(keys, forgeable) if f]
    return keys[0:]
