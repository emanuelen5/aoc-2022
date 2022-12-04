from typing import Tuple


assignment_t = slice


def is_either_fully_contained_within_other(a1: assignment_t, a2: assignment_t) -> bool:
    return (
        (a1.start >= a2.start and a1.stop <= a2.stop) or
        (a2.start >= a1.start and a2.stop <= a1.stop)
    )


def range_str_to_slice(range_str) -> assignment_t:
    d1, d2 = range_str.split("-")
    return slice(int(d1), int(d2))


def line_to_ranges(line) -> Tuple[assignment_t, assignment_t]:
    line = line.strip()
    p1, p2 = line.split(",")
    return range_str_to_slice(p1), range_str_to_slice(p2)


def has_overlap(a1: assignment_t, a2: assignment_t) -> bool:
    return (
        (a1.start <= a2.start <= a1.stop) or
        (a1.start <= a2.stop <= a1.stop)
    ) or is_either_fully_contained_within_other(a1, a2)
