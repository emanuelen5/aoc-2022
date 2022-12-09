from pathlib import Path
import unittest
import lib


with open(Path(__file__).parent.joinpath("data/test_input.txt"), 'r', encoding="utf-8") as f:
    test_input_lines = f.read().split("\n")


tc = unittest.TestCase()
tc.assertEqual((lib.Directions.right, 4), lib.Directions.parse_line(test_input_lines[0]))
tc.assertEqual([lib.Directions.right] * 4, list(lib.Directions.from_lines(test_input_lines[0:1])))

origin = lib.Pos()
tc.assertEqual([], list(lib.yield_tail_moves(origin, origin)))
tc.assertEqual([], list(lib.yield_tail_moves(lib.Pos(0, 1), origin)))
tc.assertEqual([lib.Directions.up], list(lib.yield_tail_moves(lib.Pos(0, 2), origin)))
tc.assertEqual([], list(lib.yield_tail_moves(lib.Pos(1, 1), origin)))
tc.assertEqual([lib.Directions.right, lib.Directions.up], list(lib.yield_tail_moves(lib.Pos(2, 1), origin)))

rope = lib.Rope()
tc.assertEqual((0, 0), rope.head.get_pos())
tc.assertEqual((0, 0), rope.tail.get_pos())
tc.assertEqual({(0, 0)}, rope.head.visited_positions)
tc.assertEqual({(0, 0)}, rope.tail.visited_positions)

for dir in lib.Directions.from_lines(test_input_lines):
    rope.move_head(dir)

print(rope.tail.visited_positions)
tc.assertEqual(13, len(rope.tail.visited_positions))
