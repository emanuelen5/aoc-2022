import re
from typing import List, Optional


crate_t = str
crate_stacks_t = List[List[crate_t]]
column_pattern = re.compile(r"^ *( \d+ *)+$")


def get_crates_from_line(line: str, column_count: int) -> List[crate_t]:
    crates = [None] * column_count
    for index in range(column_count):
        crate_letter_pos = 4 * index + 1
        letter = None if crate_letter_pos >= len(line) else line[crate_letter_pos]
        letter = letter if letter is not ' ' else None
        crates[index] = letter
    return crates


def is_column_index_line(line: str) -> bool:
    matches = column_pattern.finditer(line)
    return next(matches, None) is not None


def get_column_count(line: str) -> int:
    *_, last_match = column_pattern.finditer(line)
    return int(last_match.group(1))


def init_crate_stack(column_count: int) -> crate_stacks_t:
    return [[] for _ in range(column_count)]


def crate_stack_append(cs: crate_stacks_t, crates: List[Optional[crate_t]]) -> None:
    assert len(cs) == len(crates)
    for crate_stack, crate in zip(cs, crates):
        if crate is not None:
            crate_stack.append(crate)


def crate_stack_get_top(cs: crate_stacks_t) -> List[str]:
    return "".join(c[-1] for c in cs)
