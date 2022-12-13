from typing import List, Union, TypeVar, Tuple


packet_t = TypeVar("packet_t")
packet_t = List[Union[packet_t, int]]

def _from_line(packet1_line: str, packet2_line: str) -> Tuple[packet_t, packet_t]:
    return eval(packet1_line), eval(packet2_line)


def from_lines(input_lines: List[str]) -> packet_t:
    return [_from_line(packet1_line, packet2_line)
        for packet1_line, packet2_line in zip(input_lines[0::3], input_lines[1::3])]

def packet_diff(left_packet: packet_t, right_packet: packet_t) -> int:
    if isinstance(left_packet, int) and isinstance(right_packet, int):
        return left_packet - right_packet
    elif isinstance(left_packet, List) and isinstance(right_packet, List):
        for left_subpacket, right_subpacket in zip(left_packet, right_packet):
            order_diff = packet_diff(left_subpacket, right_subpacket)
            if order_diff == 0:
                continue
            return order_diff
        return len(left_packet) - len(right_packet)
    elif isinstance(left_packet, int):
        return packet_diff([left_packet], right_packet)
    elif isinstance(right_packet, int):
        return packet_diff(left_packet, [right_packet])
    raise ValueError("Unhandled case")

def is_ordered(left_packet: packet_t, right_packet: packet_t) -> bool:
    return packet_diff(left_packet, right_packet) <= 0


def part1(packet_pairs: List[Tuple[packet_t, packet_t]]) -> int:
    return sum(i+1 for i, (left_packet, right_packet) in enumerate(packet_pairs) if is_ordered(left_packet, right_packet))
