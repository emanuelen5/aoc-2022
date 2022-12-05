from pathlib import Path
import unittest
import lib


with open(Path(__file__).parent.joinpath("data/test_input.txt"), 'r', encoding="utf-8") as f:
    test_input = f.read().split("\n")

tc = unittest.TestCase()

tc.assertEqual([None, 'D', None], lib.get_crates_from_line(test_input[0], 3))
tc.assertEqual(['N', 'C', None], lib.get_crates_from_line(test_input[1], 3))
tc.assertEqual(['Z', 'M', 'P'], lib.get_crates_from_line(test_input[2], 3))

column_line = test_input[3]
tc.assertTrue(lib.is_column_index_line(column_line))
tc.assertTrue(lib.is_column_index_line(" 1   2   3   4   5   6   7   8   9"))
tc.assertEqual(3, lib.get_column_count(column_line))
tc.assertEqual(6, lib.get_column_count(" 1   2   3   4   5   6"))

cs = lib.init_crate_stack(3)
tc.assertEqual([[], [], []], cs)

crates = lib.get_crates_from_line(test_input[2], len(cs))
lib.crate_stack_append(cs, crates)
tc.assertEqual([['Z'], ['M'], ['P']], cs)
crates = lib.get_crates_from_line(test_input[1], len(cs))
lib.crate_stack_append(cs, crates)
tc.assertEqual([['Z', 'N'], ['M', 'C'], ['P']], cs)
crates = lib.get_crates_from_line(test_input[0], len(cs))
lib.crate_stack_append(cs, crates)
tc.assertEqual([['Z', 'N'], ['M', 'C', 'D'], ['P']], cs)

tc.assertEqual("NDP", lib.crate_stack_get_top(cs))

tc.assertEqual((1, 2, 1), lib.get_move_from_line(test_input[5]))
tc.assertEqual((3, 1, 3), lib.get_move_from_line(test_input[6]))
tc.assertEqual((2, 2, 1), lib.get_move_from_line(test_input[7]))

cs = [['A'], ['B'], ['C', 'D']]
tc.assertEqual([['A', 'D'], ['B'], ['C']], lib.move_stack(cs, 1, 3, 1))
tc.assertEqual([[], ['B', 'D', 'A'], ['C']], lib.move_stack(cs, 2, 1, 2))
