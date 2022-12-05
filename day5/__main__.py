from pathlib import Path
from . import lib


with open(Path(__file__).parent.joinpath("data/input.txt"), 'r', encoding="utf-8") as f:
    lines = f.read().split("\n")

for i, line in enumerate(lines):
    if lib.is_column_index_line(line):
        column_count = lib.get_column_count(lines[i])
        break
else:
    raise ValueError(f"Did not find column index line")

cs = lib.init_crate_stack(column_count)

part1 = None
part2 = None

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
