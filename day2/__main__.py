from collections import defaultdict
from pathlib import Path


from . import get_score


mapping = defaultdict(lambda: defaultdict(int))
with open(Path(__file__).parent.joinpath("input.txt")) as f:
	for line in f.readlines():
		p1, p2 = line.strip().split(" ")
		mapping[p1][p2] += 1


part1 = get_score('A', 'X')
part2 = None

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

