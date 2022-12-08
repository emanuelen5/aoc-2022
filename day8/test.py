from pathlib import Path
import unittest
import lib


with open(Path(__file__).parent.joinpath("data/test_input.txt"), 'r', encoding="utf-8") as f:
    test_input_lines = f.read().split("\n")


tc = unittest.TestCase()

map = lib.Map.from_input_lines(test_input_lines)
trees = lib.Tree(map)

for i in range(map.height):
    tc.assertTrue(trees.visible(0, i), "Left boundary")
    tc.assertTrue(trees.visible(map.width - 1, i), "Right boundary")
for i in range(map.width):
    tc.assertTrue(trees.visible(i, 0), "Top boundary")
    tc.assertTrue(trees.visible(i, map.height - 1), "Bottom boundary")

tc.assertTrue(trees.visible(1, 1))


def test_visibility(x, y, from_: set):
    dirs = {
        "left": trees.visible_from_left,
        "right": trees.visible_from_right,
        "top": trees.visible_from_top,
        "bottom": trees.visible_from_bottom,
    }
    for dir in from_:
        tc.assertTrue(dirs[dir].at(x, y), f"Tree {x},{y} is visible from {dir}")
    for dir in set(dirs.keys()) - from_:
        tc.assertFalse(dirs[dir].at(x, y), f"Tree {x},{y} is not visible from {dir}")
    tc.assertEqual(len(from_) != 0, trees.visible(x, y), f"Tree {x},{y} visibility")

test_visibility(1, 1, {"top", "left"})
test_visibility(2, 1, {"top", "right"})
test_visibility(3, 1, set())
test_visibility(1, 2, {"right"})
test_visibility(2, 2, set())
test_visibility(3, 2, {"right"})

tc.assertEqual(21, trees.get_visibility_count())

tc.assertEqual(1, trees.get_view_distance(2, 1, lib.Directions.up))
tc.assertEqual(1, trees.get_view_distance(2, 1, lib.Directions.left))
tc.assertEqual(2, trees.get_view_distance(2, 1, lib.Directions.right))
tc.assertEqual(2, trees.get_view_distance(2, 1, lib.Directions.down))

tc.assertEqual(4, trees.get_scenic_score(2, 1))
tc.assertEqual(8, trees.get_scenic_score(2, 3))

tc.assertEqual(8, trees.get_most_scenic())
