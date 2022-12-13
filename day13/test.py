from pathlib import Path
import unittest
import lib


with open(Path(__file__).parent.joinpath("data/test_input.txt"), 'r', encoding="utf-8") as f:
    test_input_lines = f.read().split("\n")


tc = unittest.TestCase()

tc.assertTrue(lib.is_ordered(1, 3), "Lower value")
tc.assertFalse(lib.is_ordered(3, 1), "Higher value")
tc.assertTrue(lib.is_ordered([1], [3]), "Equal length lists")
tc.assertFalse(lib.is_ordered([1, 3], [3]), "Longer list")
tc.assertTrue(lib.is_ordered([1], [3, 3]), "Shorter list")
tc.assertTrue(lib.is_ordered(1, [3]), "One is int, other is list")

packet_pairs = lib.from_lines(test_input_lines)
ordered_packet_index_sum = lib.part1(packet_pairs)
tc.assertEqual(13, ordered_packet_index_sum)
