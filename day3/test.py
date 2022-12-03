import unittest
import lib


tc = unittest.TestCase()
tc.assertEqual(1, lib.item_to_score('a'))
tc.assertEqual(26, lib.item_to_score('z'))
tc.assertEqual(27, lib.item_to_score('A'))
tc.assertEqual(52, lib.item_to_score('Z'))

tc.assertEqual(("vJrwpWtwJgWr", "hcsFMMfFFhFp"), lib.line_to_compartments("vJrwpWtwJgWrhcsFMMfFFhFp"))

tc.assertEqual(16, lib.compartments_to_score(*lib.line_to_compartments("vJrwpWtwJgWrhcsFMMfFFhFp")))
tc.assertEqual(38, lib.compartments_to_score(*lib.line_to_compartments("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")))
tc.assertEqual(42, lib.compartments_to_score(*lib.line_to_compartments("PmmdzqPrVvPwwTWBwg")))
tc.assertEqual(22, lib.compartments_to_score(*lib.line_to_compartments("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")))
tc.assertEqual(20, lib.compartments_to_score(*lib.line_to_compartments("ttgJtRGJQctTZtZT")))
tc.assertEqual(19, lib.compartments_to_score(*lib.line_to_compartments("CrZsJsPPZsGzwwsLwLmpwMDw")))
