from pathlib import Path
import unittest
import lib
lib.debug = True


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
