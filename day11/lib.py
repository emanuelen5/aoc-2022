from dataclasses import dataclass, field
import functools
from typing import List, Callable


class Item:
    pass


op_t = Callable[[int], int]


def create_operation(left: str, op: str, right: str) -> op_t:
    if left == "old":
        left = lambda old: old
    else:
        left_val = int(left)
        left = lambda _: left_val
    
    if op == "*":
        op = lambda l, r: l * r
    elif op == "-":
        op = lambda l, r: l - r
    elif op == "/":
        op = lambda l, r: l / r
    elif op == "+":
        op = lambda l, r: l + r
    else:
        raise ValueError(f"Unhandled operation {op!r}")

    if right == "old":
        right = lambda old: old
    else:
        right_val = int(right)
        right = lambda _: right_val

    def operation(old: int) -> int:
        return op(left(old), right(old))
    
    return operation


def parse_operation(operation_line: str) -> op_t:
    operation_line = operation_line.strip()
    assert operation_line.startswith("Operation: ")
    return create_operation(*operation_line.split()[-3:])


@dataclass
class Monkey:
    name: str
    items: List[int]
    operation: op_t = field(compare=False, repr=False)
    divisible: int = field(repr=False)
    to_if_true: int = field(repr=False)
    to_if_false: int = field(repr=False)
    monkey_list: List["Monkey"] = field(repr=False)
    inspect_count: int = 0

    def inspect_items(self, lcm: int, relief_divisor: int = 3):
        self.items = [(self.operation(item) // relief_divisor) % lcm for item in self.items]
        self.inspect_count += len(self.items)
    
    def _decision(self, item: int) -> int:
        return self.to_if_true if item % self.divisible == 0 else self.to_if_false
    
    def throw_items(self):
        thrown_items = self.items
        self.items = []
        for item in thrown_items:
            monkey = self.monkey_list[self._decision(item)]
            monkey.receive_item(item)
    
    def receive_item(self, item: int):
        self.items.append(item)

    @classmethod
    def _from_lines(cls, id_line: str, items_line: str, operation_line: str, 
                    test_line: str, true_line: str, false_line: str,
                    monkey_list: List["Monkey"]) -> "Monkey":
        return cls(
            name=int(id_line.split()[-1][:-1]),
            items=[int(v) for v in items_line[18:].replace(",", "").split()],
            operation=parse_operation(operation_line),
            divisible=int(test_line.split()[-1]),
            to_if_true=int(true_line.split()[-1]),
            to_if_false=int(false_line.split()[-1]),
            monkey_list=monkey_list
        )

    @classmethod
    def from_lines(cls, input_lines: List[str]) -> List["Monkey"]:
        monkey_lines = zip(
            input_lines[0::7], input_lines[1::7], input_lines[2::7], 
            input_lines[3::7], input_lines[4::7], input_lines[5::7])
        
        monkey_list = []  # Keep self references
        monkeys = [cls._from_lines(*lines, monkey_list) for lines in monkey_lines]
        for monkey in monkeys:
            monkey_list.append(monkey)
        return monkeys


def monkey_lcm(monkeys: List[Monkey]) -> int:
    return functools.reduce(lambda x, y: x * y, [monkey.divisible for monkey in monkeys])

def run_round_part1(monkeys: List[Monkey]):
    lcm = monkey_lcm(monkeys)
    for monkey in monkeys:
        monkey.inspect_items(lcm)
        monkey.throw_items()

def run_round_part2(monkeys: List[Monkey]):
    lcm = monkey_lcm(monkeys)
    for monkey in monkeys:
        monkey.inspect_items(lcm, relief_divisor=1)
        monkey.throw_items()

def metric(monkeys: List[Monkey]):
    inspect_counts = sorted(monkey.inspect_count for monkey in monkeys)
    return inspect_counts[-2] * inspect_counts[-1]
