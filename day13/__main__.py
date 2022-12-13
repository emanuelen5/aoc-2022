from pathlib import Path
from . import lib


with open(Path(__file__).parent.joinpath("data/input.txt"), 'r', encoding="utf-8") as f:
    lines = f.read().split("\n")

packet_pairs = lib.packet_pairs_from_lines(lines)

part1 = lib.part1(packet_pairs)

packet_list = lib.packet_pairs_to_list(packet_pairs)
part2 = lib.part2(packet_list)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
