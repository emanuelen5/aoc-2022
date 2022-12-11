from pathlib import Path
from . import lib


with open(Path(__file__).parent.joinpath("data/input.txt"), 'r', encoding="utf-8") as f:
    lines = f.read().split("\n")

monkeys = lib.Monkey.from_lines(lines)
for _ in range(20):
    lib.run_round_part1(monkeys)

part1 = lib.metric(monkeys)

monkeys = lib.Monkey.from_lines(lines)
for i in range(10000):
    lib.run_round_part2(monkeys)

part2 = lib.metric(monkeys)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
