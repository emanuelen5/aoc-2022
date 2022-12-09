from dataclasses import dataclass, field
from enum import Enum
from typing import Tuple, List, Iterator, Set


class Directions(Enum):
    up = "U"
    down = "D"
    left = "L"
    right = "R"

    def to_diff(self) -> Tuple[int, int]:
        if self is self.up:
            return (0, 1)
        elif self is self.down:
            return (0, -1)
        elif self is self.left:
            return (-1, 0)
        elif self is self.right:
            return (1, 0)
    
    @classmethod
    def parse_line(cls, line: str) -> Tuple["Directions", int]:
        dir, times = line.split()
        return cls(dir), int(times)
    
    @classmethod
    def from_lines(cls, input_lines: List[str]) -> Iterator["Directions"]:
        for line in input_lines:
            dir, times = cls.parse_line(line)
            for _ in range(times):
                yield dir


@dataclass
class Pos:
    x: int = 0
    y: int = 0
    visited_positions: Set[Tuple[int, int]] = field(default_factory=lambda: {(0, 0)}, repr=False)

    def get_pos(self) -> Tuple[int, int]:
        return self.x, self.y

    def move(self, dir: Directions):
        dx, dy = dir.to_diff()
        self.x += dx
        self.y += dy
        self.visited_positions.add(self.get_pos())
        print("Pos: ", self.x, self.y)

    def diff(self, other: "Pos") -> Tuple[int, int]:
        return other.x - self.x, other.y - self.y


def yield_tail_moves(head: Pos, tail: Pos) -> Iterator[Directions]:
    dx, dy = tail.diff(head)
    if (abs(dx) <= 1 and abs(dy) <= 1):
        return  # Yield nothing
    if dx:
        yield Directions.right if dx > 0 else Directions.left
    if dy:
        yield Directions.up if dy > 0 else Directions.down


@dataclass
class Rope:
    head: Pos = field(default_factory=lambda: Pos())
    tail: Pos = field(default_factory=lambda: Pos())

    def move_head(self, dir: Directions):
        self.head.move(dir)
        for dir in yield_tail_moves(self.head, self.tail):
            self.tail.move(dir)
