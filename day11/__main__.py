from pathlib import Path
from . import lib


with open(Path(__file__).parent.joinpath("data/input.txt"), 'r', encoding="utf-8") as f:
    lines = f.read().split("\n")

monkeys = lib.Monkey.from_lines(lines)
for _ in range(20):
    lib.run_round(monkeys)

part1 = lib.part1_metric(monkeys)
part2 = None

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
