from pathlib import Path
from . import lib


with open(Path(__file__).parent.joinpath("data/input.txt"), 'r', encoding="utf-8") as f:
    lines = f.read().split("\n")

state = lib.State()
for instr in (lib.line_to_instruction(line) for line in lines):
    state.run_instruction(instr)

part1 = state.calculate_part1()
part2 = None

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
