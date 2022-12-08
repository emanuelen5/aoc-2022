from array import array
from enum import Enum
from dataclasses import dataclass
import math
from typing import List, Tuple


@dataclass  # For compare method
class Map:
    values: List[array]
    height: int = 0
    width: int = 0

    def __init__(self, width, height):
        row_init = b'\0' * width
        self.width = width
        self.height = height
        self.values = [array('B', row_init) for _ in range(height)]
    
    @classmethod
    def from_input_lines(cls, lines: List[str]) -> "Map":
        height = len(lines)
        width = len(lines[0])
        inst = cls(width, height)
        for i, row in enumerate(lines):
            for j, v in enumerate(row):
                inst.set(j, i, int(v))
        return inst
    
    def at(self, x, y) -> int:
        return self.values[y][x]
    
    def set(self, x, y, value: int):
        self.values[y][x] = value


class BoolMap(Map):
    pass


class Directions(Enum):
    up = "up"
    down = "down"
    left = "left"
    right = "right"

    def to_diff(self) -> Tuple[int, int]:
        if self is self.up:
            return (0, -1)
        elif self is self.down:
            return (0, 1)
        elif self is self.left:
            return (-1, 0)
        elif self is self.right:
            return (1, 0)


class Tree:
    def __init__(self, map: Map):
        self.map = map
        self.visible_from_left = BoolMap(map.width, map.height)
        self.visible_from_right = BoolMap(map.width, map.height)
        self.visible_from_top = BoolMap(map.width, map.height)
        self.visible_from_bottom = BoolMap(map.width, map.height)
        self.calculate_visibility()

    def calculate_visibility(self):
        # Forward pass
        height_per_row = [0] * self.map.height
        height_per_col = [0] * self.map.width
        for i, row in enumerate(self.map.values):
            for j, height in enumerate(row):
                row_height = height_per_row[i]
                col_height = height_per_col[j]
                if height > row_height:
                    # print("Visible from left", j, i, "at height", height)
                    self.visible_from_left.set(j, i, height)
                    height_per_row[i] = height
                if height > col_height:
                    # print("Visible from top", j, i, "at height", height)
                    self.visible_from_top.set(j, i, height)
                    height_per_col[j] = height
        
        # Backward pass
        height_per_row = [0] * self.map.height
        height_per_col = [0] * self.map.width
        for i, row in reversed(list(enumerate(self.map.values))):
            for j, height in reversed(list(enumerate(row))):
                row_height = height_per_row[i]
                col_height = height_per_col[j]
                if height > row_height:
                    # print("Visible from right", j, i, "at height", height)
                    self.visible_from_right.set(j, i, height)
                    height_per_row[i] = height
                if height > col_height:
                    # print("Visible from bottom", j, i, "at height", height)
                    self.visible_from_bottom.set(j, i, height)
                    height_per_col[j] = height
    
    def get_view_distance(self, x: int, y: int, direction: Directions) -> int:
        dx, dy = direction.to_diff()
        h0 = self.map.at(x, y)
        view_count = 0
        x += dx
        y += dy
        while (0 <= y < self.map.height) and (0 <= x < self.map.width):
            view_count += 1
            if self.map.at(x, y) >= h0:
                break
            x += dx
            y += dy
        return view_count

    def get_scenic_score(self, x: int, y: int) -> int:
        return math.prod(self.get_view_distance(x, y, dir) for dir in Directions)

    def get_most_scenic(self) -> int:
        return max(max(self.get_scenic_score(x, y) for x in range(self.map.width)) for y in range(self.map.height))

    def visible(self, x, y) -> bool:
        if (0 < x < self.map.width - 1) and (0 < y < self.map.height - 1):
            return bool(
                self.visible_from_left.at(x, y) or self.visible_from_right.at(x, y) 
                or self.visible_from_top.at(x, y) or self.visible_from_bottom.at(x, y))
        return True
    
    def get_visibility_count(self) -> int:
        return sum(sum(1 for x in range(self.map.width) if self.visible(x, y)) for y in range(self.map.height))
