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
        return self.manhattan_distance(pos) >= self.distance
    
    def coverage_of_line(self, y: int) -> slice:
        dy = abs(self.pos.y - y)

        # Does not cover lines at all
        if self.distance < dy:
            return (0, -1)

        dx = abs(self.distance - dy)
        x_min = self.pos.x - dx
        x_max = self.pos.x + dx

        return x_min, x_max


def can_have_sensor(sensors: List[Sensor], pos: Pos) -> bool:
    for sensor in sensors:
        if not sensor.can_have_sensor(pos):
            return False
    return True


def part1(sensors: List[Sensor], y_line: int) -> int:
    min_x, max_x = sensors[0].coverage_of_line(y_line)
    for sensor in sensors[1:]:
        _min_x, _max_x = sensor.coverage_of_line(y_line)
        min_x = min(min_x, _min_x)
        max_x = max(max_x, _max_x)
    
    return sum(1 for x in range(min_x, max_x + 1) if not can_have_sensor(sensors, Pos(x, y_line)))
