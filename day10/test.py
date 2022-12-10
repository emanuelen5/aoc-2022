from pathlib import Path
import unittest
import lib


with open(Path(__file__).parent.joinpath("data/test_input.txt"), 'r', encoding="utf-8") as f:
    test_input_lines = f.read().split("\n")
with open(Path(__file__).parent.joinpath("data/test_input2.txt"), 'r', encoding="utf-8") as f:
    test_input_lines2 = f.read().split("\n")


tc = unittest.TestCase()

state = lib.State()
x_init = state.x
state.run_instruction(lib.Nop())
state.run_instruction(lib.Nop())
tc.assertEqual(x_init, state.x)
tc.assertEqual(3, state.cycle)

tc.assertEqual(lib.Nop(), lib.line_to_instruction(test_input_lines[0]))
tc.assertEqual(lib.AddX(3), lib.line_to_instruction(test_input_lines[1]))
tc.assertEqual(lib.AddX(-5), lib.line_to_instruction(test_input_lines[2]))

state = lib.State()
for instr in (lib.line_to_instruction(line) for line in test_input_lines2):
    state.run_instruction(instr)

tc.assertEqual(13140, state.calculate_part1())
