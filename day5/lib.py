import re
from typing import List, Optional, Tuple


crate_t = str
crate_stacks_t = List[List[crate_t]]
column_pattern = re.compile(r"^ *( \d+ *)+$")
move_pattern = re.compile(r"^move (\d+) from (\d+) to (\d+)$")


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


def crate_stack_append(cs: crate_stacks_t, crates: List[Optional[crate_t]]) -> crate_stacks_t:
    assert len(cs) == len(crates)
    for crate_stack, crate in zip(cs, crates):
        if crate is not None:
            crate_stack.append(crate)
    return cs


def crate_stack_get_top(cs: crate_stacks_t) -> List[str]:
    return "".join(c[-1] for c in cs)


def get_move_from_line(line: str) -> Tuple[int, int, int]:
    match = move_pattern.match(line)
    numbers_strs = [match.group(1), match.group(2), match.group(3)]
    return tuple([int(n) for n in numbers_strs])


def move_stack(cs: crate_stacks_t, count: int, from_: int, to: int) -> None:
    from_stack = cs[from_ - 1]
    to_stack = cs[to - 1]
    for _ in range(count):
        to_stack.append(from_stack.pop())
    return cs
