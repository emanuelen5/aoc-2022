from pathlib import Path
from . import lib


with open(Path(__file__).parent.joinpath("input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

compartments = [lib.line_to_compartments(line) for line in lines]
groups = lib.group_lines(lines)


part1 = sum(lib.compartments_to_score(c1, c2) for c1, c2 in compartments)
part2 = sum(lib.group_to_score(group) for group in groups)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
