from pathlib import Path
from . import lib


with open(Path(__file__).parent.joinpath("data/input.txt"), 'r', encoding="utf-8") as f:
    assignments = [lib.line_to_ranges(line) for line in f.readlines()]

fully_contained_ranges = sum(1 for a1, a2 in assignments if lib.is_either_fully_contained_within_other(a1, a2))
partially_overlapping_ranges = sum(1 for a1, a2 in assignments if lib.has_overlap(a1, a2))

part1 = fully_contained_ranges
part2 = partially_overlapping_ranges

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
