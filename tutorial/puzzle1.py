from typing import List, Optional


def is_ordered_key(segments: str) -> bool:
    for i in range(1, len(segments)):
        if ord(segments[i]) < ord(segments[i - 1]):
            return False
    return True


def find_ordered_key(keys: List[str]) -> Optional[str]:
    for k in keys:
        if is_ordered_key(k.strip()):
            return k
    return None
