from pathlib import Path
from . import lib
from copy import deepcopy


with open(Path(__file__).parent.joinpath("data/input.txt"), 'r', encoding="utf-8") as f:
    lines = f.read().split("\n")

for i, line in enumerate(lines):
    if lib.is_column_index_line(line):
        column_count = lib.get_column_count(lines[i])
        last_row_line = i
        first_move_line = i + 2
        break
else:
    raise ValueError(f"Did not find column index line")

cs = lib.init_crate_stack(column_count)
for line in lines[last_row_line - 1::-1]:
    crates = lib.get_crates_from_line(line, column_count)
    lib.crate_stack_append(cs, crates)

cs_9001 = deepcopy(cs)

for line in lines[first_move_line:]:
    count, from_, to = lib.get_move_from_line(line)
    lib.move_stack(cs, count, from_, to)
    lib.move_stack_9001(cs_9001, count, from_, to)

part1 = lib.crate_stack_get_top(cs)
part2 = lib.crate_stack_get_top(cs_9001)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
