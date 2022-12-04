from pathlib import Path
import unittest
import lib


with open(Path(__file__).parent.joinpath("data/test_input.txt"), 'r', encoding="utf-8") as f:
    test_input = [line.strip() for line in f.readlines()]


tc = unittest.TestCase()

tc.assertEqual(slice(2, 4), lib.range_str_to_slice("2-4"), "One digit each")
tc.assertEqual(slice(11, 50), lib.range_str_to_slice("11-50"), "Two digits")

tc.assertEqual((slice(2, 4), slice(6, 8)), lib.line_to_ranges(test_input[0]))

tc.assertFalse(lib.is_either_fully_contained_within_other(*lib.line_to_ranges(test_input[0])))
tc.assertFalse(lib.is_either_fully_contained_within_other(*lib.line_to_ranges(test_input[1])))
tc.assertFalse(lib.is_either_fully_contained_within_other(*lib.line_to_ranges(test_input[2])))
tc.assertTrue(lib.is_either_fully_contained_within_other(*lib.line_to_ranges(test_input[3])))
tc.assertTrue(lib.is_either_fully_contained_within_other(*lib.line_to_ranges(test_input[4])))
tc.assertFalse(lib.is_either_fully_contained_within_other(*lib.line_to_ranges(test_input[5])))

tc.assertFalse(lib.has_overlap(*lib.line_to_ranges(test_input[0])))
tc.assertFalse(lib.has_overlap(*lib.line_to_ranges(test_input[1])))
tc.assertTrue(lib.has_overlap(*lib.line_to_ranges(test_input[2])))
tc.assertTrue(lib.has_overlap(*lib.line_to_ranges(test_input[3])))
tc.assertTrue(lib.has_overlap(*lib.line_to_ranges(test_input[4])))
tc.assertTrue(lib.has_overlap(*lib.line_to_ranges(test_input[5])))
