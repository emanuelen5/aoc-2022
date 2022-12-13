from typing import List, Union, TypeVar, Tuple


packet_t = TypeVar("packet_t")
packet_t = List[Union[packet_t, int]]

def _from_line(packet1_line: str, packet2_line: str) -> Tuple[packet_t, packet_t]:
    return eval(packet1_line), eval(packet2_line)


def from_lines(input_lines: List[str]) -> packet_t:
    packet_lines = zip(input_lines[0::3], input_lines[1::3])
    
    packet_pairs = []
    for packet1_line, packet2_line in packet_lines:
        packet_pairs.append(_from_line(packet1_line, packet2_line))
    return packet_pairs


def is_ordered(left_packet: packet_t, right_packet: packet_t) -> bool:
    if isinstance(left_packet, int) and isinstance(right_packet, int):
        return left_packet < right_packet
    elif isinstance(left_packet, List) and isinstance(right_packet, List):
        if len(left_packet) < len(right_packet):
            return True
        elif len(left_packet) == len(right_packet):
            for left_subpacket, right_subpacket in zip(left_packet, right_packet):
                if not is_ordered(left_subpacket, right_subpacket):
                    return False
            return True
        return False
    elif isinstance(left_packet, int):
        return is_ordered([left_packet], right_packet)
    elif isinstance(right_packet, int):
        return is_ordered(left_packet, [right_packet])


def part1(packet_pairs: List[Tuple[packet_t, packet_t]]) -> int:
    return sum(i+1 for i, (left_packet, right_packet) in enumerate(packet_pairs) if is_ordered(left_packet, right_packet))
