from pathlib import Path
from . import lib


with open(Path(__file__).parent.joinpath("data/input.txt"), 'r', encoding="utf-8") as f:
    lines = f.read().split("\n")

packet_pairs = lib.from_lines(lines)

part1 = lib.part1(packet_pairs)
part2 = None

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
