from dataclasses import dataclass, field
from typing import List, Callable
debug = False


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
    divisible: int
    to_if_true: int
    to_if_false: int
    monkey_list: List["Monkey"]
    inspect_count: int = 0

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
