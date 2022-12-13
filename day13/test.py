from pathlib import Path
import unittest
import lib


with open(Path(__file__).parent.joinpath("data/test_input.txt"), 'r', encoding="utf-8") as f:
    test_input_lines = f.read().split("\n")


tc = unittest.TestCase()

tc.assertTrue(lib.is_ordered(1, 3), "Lower value")
tc.assertFalse(lib.is_ordered(3, 1), "Higher value")
tc.assertTrue(lib.is_ordered([1], [3]), "Equal length lists")
tc.assertFalse(lib.is_ordered([1, 3], [1]), "Longer list")
tc.assertTrue(lib.is_ordered([3], [3, 3]), "Shorter list")
tc.assertTrue(lib.is_ordered(1, [3]), "One is int, other is list")
tc.assertFalse(lib.is_ordered([9], [8,7,6]), "Higher value in short list")

packet_pairs = lib.from_lines(test_input_lines)
tc.assertTrue(lib.is_ordered(*packet_pairs[0]))
tc.assertTrue(lib.is_ordered(*packet_pairs[1]))
tc.assertFalse(lib.is_ordered(*packet_pairs[2]))
tc.assertTrue(lib.is_ordered(*packet_pairs[3]))
tc.assertFalse(lib.is_ordered(*packet_pairs[4]), "Right side ran out of items")
tc.assertTrue(lib.is_ordered(*packet_pairs[5]))
tc.assertFalse(lib.is_ordered(*packet_pairs[6]))
tc.assertFalse(lib.is_ordered(*packet_pairs[7]))

ordered_packet_index_sum = lib.part1(packet_pairs)
tc.assertEqual(13, ordered_packet_index_sum)
