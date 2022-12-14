from dataclasses import dataclass, field
from typing import List, Union, Optional


class Instruction:
    exec_time: int = 1

    def __init__(self):
        self.delay = self.exec_time

    def cycle(self) -> bool:
        self.delay -= 1

    @property
    def is_finished(self) -> bool:
        return self.delay <= 0


class Nop(Instruction):
    def __eq__(self, other: object) -> bool:
        return isinstance(other, self.__class__)
    
    def __repr__(self) -> str:
        return f"<Nop>"


class AddX(Instruction):
    exec_time = 2

    def __init__(self, value: int):
        super().__init__()
        self.V = value
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, self.__class__) and self.V == other.V
    
    def __repr__(self) -> str:
        return f"<AddX V={self.V}, {self.delay}>"


instr_t = Union[Nop, AddX]
def line_to_instruction(line: str) -> instr_t:
    if line == "noop":
        return Nop()
    op, arg = line.split()
    if op == "addx":
        return AddX(int(arg))
    raise ValueError(f"Unknown operation {line}")


@dataclass
class CRT:
    cols = 40
    rows = 6
    cycle: int = 1
    pixels: List[int] = field(default_factory=lambda: [None] * CRT.cols * CRT.rows, repr=False)

    def run_cycle(self, x: int):
        crt_col = self.cycle % self.cols
        pixel_index = self.cycle - 1
        self.pixels[pixel_index] = x - 1 <= crt_col <= x + 1
        self.cycle += 1
    
    def get_pixel(self, x, y):
        return self.pixels[y * self.cols + x]

    def __str__(self) -> str:
        s = ""
        for y in range(self.rows):
            s += "|"
            for x in range(self.cols):
                pixel = self.get_pixel(x, y)
                s += " " if pixel is None else "#" if pixel else "."
            s += "|\n"
        return s


@dataclass
class State:
    cycle: int = 1
    x: int = 1
    current_instruction: Optional[instr_t] = field(default=None)
    signal_strengths: List[int] = field(default_factory=lambda: [], repr=False)
    crt: CRT = field(default_factory=lambda: CRT())

    def needs_instruction(self) -> bool:
        return self.current_instruction is None or self.current_instruction.is_finished
    
    def run_cycle(self):
        self.current_instruction.cycle()

        if self.cycle in {20, 60, 100, 140, 180, 220}:
            self.signal_strengths.append(self.get_current_signal_strength())

        if self.current_instruction.is_finished:
            self.instruction_semantics(self.current_instruction)

        self.crt.run_cycle(self.x)
        self.cycle += 1

    def run_instruction(self, instr: instr_t):
        self.current_instruction = instr
        while not self.needs_instruction():
            self.run_cycle()
    
    def get_current_signal_strength(self) -> int:
        s = self.cycle * self.x
        # print("Signal strength: ", self.cycle, self.x, s)
        return s
    
    def instruction_semantics(self, instr: instr_t):
        if isinstance(instr, Nop):
            pass
        elif isinstance(instr, AddX):
            self.x += instr.V
        
    def calculate_part1(self) -> int:
        return sum(self.signal_strengths)
