from dataclasses import dataclass
import re
from typing import List


sensor_line_re = re.compile(f"^.+x=(-?\d+), y=(-?\d+):.+x=(-?\d+), y=(-?\d+)$")


@dataclass
class Pos:
    x: int
    y: int

    def manhattan_distance(self, pos: "Pos"):
        return abs(self.x - pos.x) + abs(self.y - pos.y)
    
    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Sensor:
    pos: Pos
    beacon: Pos

    def __post_init__(self):
        self.distance = self.pos.manhattan_distance(self.beacon)

    def manhattan_distance(self, pos: Pos):
        return self.pos.manhattan_distance(pos)
    

    @classmethod
    def create(cls, sx: int, sy: int, bx: int, by: int) -> "Sensor":
        return cls(Pos(sx, sy), Pos(bx, by))
    

    @classmethod
    def from_lines(cls, lines: List[str]) -> List["Sensor"]:
        sensors =  []
        for line in lines:
            m = sensor_line_re.match(line)
            assert m is not None, f"No match for line {line!r}"
            sx, sy, bx, by = tuple(int(m.group(i)) for i in range(1, 5))
            sensors.append(cls(
                pos=Pos(sx, sy),
                beacon=Pos(bx, by)
            ))
        return sensors
    
    def can_have_sensor(self, pos: Pos) -> bool:
        return self.manhattan_distance(pos) > self.distance
    
    def coverage_of_line(self, y: int) -> slice:
        dy = abs(self.pos.y - y)

        # Does not cover lines at all
        if self.distance < dy:
            return (0, -1)

        dx = abs(self.distance - dy - 1) + 1
        x_min = self.pos.x - dx
        x_max = self.pos.x + dx

        return x_min, x_max


def can_have_sensor(sensors: List[Sensor], pos: Pos) -> bool:
    for sensor in sensors:
        if not sensor.can_have_sensor(pos):
            return False
    return True


def draw(sensors: List[Sensor], xrange: slice, yrange: slice):
    sensor_positions = [s.pos for s in sensors]
    beacon_positions = [s.beacon for s in sensors]
    rows = 3
    x_numbers = [f"{x:-3}" for x in range(xrange.start, xrange.stop)]
    for row in range(rows):
        line = "   "
        for i, x in enumerate(range(xrange.start, xrange.stop)):
            if (x % 5) == 0:
                line += x_numbers[i][row]
            else:
                line += " "
        print(line)
    for y in range(yrange.start, yrange.stop):
        line = f"{y:2} "
        for x in range(xrange.start, xrange.stop):
            if any(pos.x == x and pos.y == y for pos in sensor_positions):
                line += "S"
            elif any(pos.x == x and pos.y == y for pos in beacon_positions):
                line += "B"
            elif not can_have_sensor(sensors, Pos(x, y)):
                line += "#"
            else:
                line += "."
        print(line)


def part1(sensors: List[Sensor], y_line: int) -> int:
    min_x, max_x = sensors[0].coverage_of_line(y_line)
    for sensor in sensors[1:]:
        _min_x, _max_x = sensor.coverage_of_line(y_line)
        min_x = min(min_x, _min_x)
        max_x = max(max_x, _max_x)
    
    covered = sum(1 for x in range(min_x, max_x + 1) if not can_have_sensor(sensors, Pos(x, y_line)))

    # Remove positions where sensors or beacons already exist
    duplicates = 0
    positions = set(s.pos for s in sensors).union(set(s.beacon for s in sensors))
    for pos in positions:
        if y_line == pos.y and not can_have_sensor(sensors, Pos(pos.x, pos.y)):
            duplicates += 1

    return covered - duplicates
