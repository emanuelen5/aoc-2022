from functools import lru_cache
from typing import Tuple


@lru_cache()
def item_to_score(item: str):
    if ord('a') <= ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1
    if ord('A') <= ord(item) <= ord('Z'):
        return ord(item) - ord('A') + 27


def line_to_compartments(line) -> Tuple[str, str]:
    line = line.strip()
    line_len = len(line) // 2
    c1 = line[:line_len]
    c2 = line[-line_len:]
    return c1, c2


def compartments_to_score(c1, c2) -> int:
    duplicate_items = set(c1).intersection(set(c2))
    assert len(duplicate_items) == 1, "Only one item should be common between the compartments"
    return item_to_score(next(i for i in duplicate_items))
