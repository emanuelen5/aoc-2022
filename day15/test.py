from pathlib import Path
import unittest
import lib


with open(Path(__file__).parent.joinpath("data/test_input.txt"), 'r', encoding="utf-8") as f:
    test_input_lines = f.read().split("\n")

sensors = lib.Sensor.from_lines(test_input_lines)


tc = unittest.TestCase()
tc.assertEqual(14, len(sensors))
tc.assertEqual(lib.Sensor(lib.Pos(2, 18), lib.Pos(-2, 15)), sensors[0])

tc.assertEqual(5, lib.Pos(0, 0).manhattan_distance(lib.Pos(5, 0)))
tc.assertEqual(5, lib.Pos(0, 0).manhattan_distance(lib.Pos(0, 5)))
tc.assertEqual(5, lib.Pos(5, 0).manhattan_distance(lib.Pos(0, 0)))
tc.assertEqual(5, lib.Pos(0, 5).manhattan_distance(lib.Pos(0, 0)))

tc.assertFalse(lib.Sensor.create(0, 0, 5, 0).can_have_sensor(lib.Pos(0, 0)))
tc.assertTrue(lib.Sensor.create(0, 0, 5, 0).can_have_sensor(lib.Pos(6, 0)))
tc.assertTrue(lib.Sensor.create(0, 0, 5, 0).can_have_sensor(lib.Pos(5, 1)))

tc.assertEqual((-1, 1), lib.Sensor.create(0, 0, 1, 0).coverage_of_line(0))
tc.assertEqual((-1, 1), lib.Sensor.create(0, 0, 0, 1).coverage_of_line(0))
tc.assertEqual((-1, 1), lib.Sensor.create(0, 2, 0, -1).coverage_of_line(0))
tc.assertEqual((0, -1), lib.Sensor.create(0, 2, 0, 1).coverage_of_line(0), "No coverage")

# test_sensors = [
#     lib.Sensor.create(-10, 1, -10, 0),
#     lib.Sensor.create(),
# ]
# tc.assertEqual(2, lib.part1(test_sensors, 0)

tc.assertEqual(26, lib.part1(sensors, 10))
