from pathlib import Path
import unittest
import lib


with open(Path(__file__).parent.joinpath("test_input.txt"), 'r') as f:
    test_input_lines = [line.strip() for line in f.readlines()]


tc = unittest.TestCase()
tc.assertEqual(1, lib.item_to_score('a'))
tc.assertEqual(26, lib.item_to_score('z'))
tc.assertEqual(27, lib.item_to_score('A'))
tc.assertEqual(52, lib.item_to_score('Z'))

tc.assertEqual(("vJrwpWtwJgWr", "hcsFMMfFFhFp"), lib.line_to_compartments(test_input_lines[0]))

tc.assertEqual(16, lib.compartments_to_score(*lib.line_to_compartments(test_input_lines[0])))
tc.assertEqual(38, lib.compartments_to_score(*lib.line_to_compartments(test_input_lines[1])))
tc.assertEqual(42, lib.compartments_to_score(*lib.line_to_compartments(test_input_lines[2])))
tc.assertEqual(22, lib.compartments_to_score(*lib.line_to_compartments(test_input_lines[3])))
tc.assertEqual(20, lib.compartments_to_score(*lib.line_to_compartments(test_input_lines[4])))
tc.assertEqual(19, lib.compartments_to_score(*lib.line_to_compartments(test_input_lines[5])))

# Part 2
groups = list(lib.group_lines(test_input_lines))
tc.assertEqual([
    (test_input_lines[0], test_input_lines[1], test_input_lines[2]), 
    (test_input_lines[3], test_input_lines[4], test_input_lines[5])
    ], groups)
tc.assertEqual(18, lib.group_to_score(groups[0]))
tc.assertEqual(52, lib.group_to_score(groups[1]))
