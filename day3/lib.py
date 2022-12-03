from functools import lru_cache
from typing import Tuple, List, Set


@lru_cache()
def item_to_score(item: str):
    if ord('a') <= ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1
    if ord('A') <= ord(item) <= ord('Z'):
        return ord(item) - ord('A') + 27
    raise ValueError(f"Unhandled value {item}")


def line_to_compartments(line) -> Tuple[str, str]:
    line = line.strip()
    line_len = len(line) // 2
    c1 = line[:line_len]
    c2 = line[-line_len:]
    return c1, c2


def common_item_to_score(item_set: Set[str]) -> int:
    assert len(item_set) == 1, "Only one item should be common to be able to calculate the score"
    return item_to_score(next(i for i in item_set))


def compartments_to_score(c1, c2) -> int:
    duplicate_items = set(c1).intersection(set(c2))
    return common_item_to_score(duplicate_items)


group_t = Tuple[str, str, str]

def group_lines(lines) -> List[group_t]:
    return zip(lines[::3], lines[1::3], lines[2::3])

def group_to_score(group: group_t) -> int:
    duplicate_items = set(group[0]).intersection(group[1]).intersection(group[2])
    return common_item_to_score(duplicate_items)
