from collections import defaultdict
from pathlib import Path


from . import lib


mapping = defaultdict(lambda: defaultdict(int))
with open(Path(__file__).parent.joinpath("input.txt")) as f:
	for line in f.readlines():
		p1, p2 = line.strip().split(" ")
		mapping[p1][p2] += 1


part1 = 0
for p1, to in mapping.items():
	for p2, count in to.items():
		part1 += count * lib.get_score(p1, p2)

part2 = 0
for p1, to in mapping.items():
	for p2, count in to.items():
		part2 += count * lib.get_score(p1, lib.get_shape_for_outcome(p1, p2))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
