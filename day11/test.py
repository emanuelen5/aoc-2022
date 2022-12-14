from pathlib import Path
import unittest
import lib


with open(Path(__file__).parent.joinpath("data/test_input.txt"), 'r', encoding="utf-8") as f:
    test_input_lines = f.read().split("\n")

tc = unittest.TestCase()

tc.assertEqual(1, lib.create_operation("old", "*", "old")(1))
tc.assertEqual(4, lib.create_operation("old", "*", "old")(2))
tc.assertEqual(9, lib.create_operation("old", "*", "3")(3))
tc.assertEqual(0, lib.create_operation("old", "-", "1")(1))
tc.assertEqual(5, lib.create_operation("old", "+", "2")(3))

tc.assertEqual(79 * 19, lib.parse_operation(test_input_lines[2])(79))
tc.assertEqual(54 + 6, lib.parse_operation(test_input_lines[9])(54))
tc.assertEqual(79 * 79, lib.parse_operation(test_input_lines[16])(79))

monkeys = lib.Monkey.from_lines(test_input_lines)
tc.assertEqual(4, len(monkeys))
tc.assertEqual([79, 98], monkeys[0].items)
tc.assertEqual(23, monkeys[0].divisible)
tc.assertEqual(2, monkeys[0].to_if_true)
tc.assertEqual(3, monkeys[0].to_if_false)

lib.run_round_part1(monkeys)
tc.assertEqual([20, 23, 27, 26], monkeys[0].items)
tc.assertEqual([2080, 25, 167, 207, 401, 1046], monkeys[1].items)
tc.assertEqual([], monkeys[2].items)
tc.assertEqual([], monkeys[3].items)

for _ in range(20-1):
    lib.run_round_part1(monkeys)

tc.assertEqual(10605, lib.metric(monkeys))

# Part 2
monkeys = lib.Monkey.from_lines(test_input_lines)

lib.run_round_part2(monkeys)
tc.assertEqual([2, 4, 3, 6], [monkey.inspect_count for monkey in monkeys])
for _ in range(19):
    lib.run_round_part2(monkeys)
tc.assertEqual([99, 97, 8, 103], [monkey.inspect_count for monkey in monkeys])
