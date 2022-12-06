from pathlib import Path
import unittest
import lib


with open(Path(__file__).parent.joinpath("data/test_input.txt"), 'r', encoding="utf-8") as f:
    test_input_lines = f.read().split("\n")


tc = unittest.TestCase()
tc.assertEqual(7, lib.get_start_of_packet_end(test_input_lines[0]))
tc.assertEqual(5, lib.get_start_of_packet_end(test_input_lines[1]))
tc.assertEqual(6, lib.get_start_of_packet_end(test_input_lines[2]))
tc.assertEqual(10, lib.get_start_of_packet_end(test_input_lines[3]))
tc.assertEqual(11, lib.get_start_of_packet_end(test_input_lines[4]))

tc.assertEqual(19, lib.get_start_of_packet_end(test_input_lines[0], 14))
tc.assertEqual(23, lib.get_start_of_packet_end(test_input_lines[1], 14))
tc.assertEqual(23, lib.get_start_of_packet_end(test_input_lines[2], 14))
tc.assertEqual(29, lib.get_start_of_packet_end(test_input_lines[3], 14))
tc.assertEqual(26, lib.get_start_of_packet_end(test_input_lines[4], 14))
