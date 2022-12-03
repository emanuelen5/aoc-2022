from pathlib import Path
from . import lib


with open(Path(__file__).parent.joinpath("input.txt")) as f:
	compartments = [lib.line_to_compartments(line) for line in f.readlines()]


part1 = sum(lib.compartments_to_score(c1, c2) for c1, c2 in compartments)
part2 = None

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
