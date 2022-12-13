from copy import deepcopy
from functools import cmp_to_key
from typing import List, Union, TypeVar, Tuple, Iterator


packet_t = TypeVar("packet_t")
packet_t = List[Union[packet_t, int]]

def _from_line(packet1_line: str, packet2_line: str) -> Tuple[packet_t, packet_t]:
    return eval(packet1_line), eval(packet2_line)


def packet_pairs_from_lines(input_lines: List[str]) -> List[Tuple[packet_t, packet_t]]:
    return [_from_line(packet1_line, packet2_line)
        for packet1_line, packet2_line in zip(input_lines[0::3], input_lines[1::3])]


def packet_pairs_to_list(packet_pairs: List[Tuple[packet_t, packet_t]]) -> List[packet_t]:
    def unpack_gen(packet_pair_list) -> Iterator[packet_t]:
        for packet1, packet2 in packet_pair_list:
            yield packet1
            yield packet2
    return list(unpack_gen(packet_pairs))


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

def sort_packet_list(packet_list: List[packet_t]) -> List[packet_t]:
    return sorted(packet_list, key=cmp_to_key(packet_diff)) 

def part2(packet_list: List[packet_t]) -> int:
    key1 = [[2]]
    key2 = [[6]]
    packet_list.append(key1)
    packet_list.append(key2)
    sorted_list = sort_packet_list(packet_list)
    index1 = sorted_list.index(key1) + 1
    index2 = sorted_list.index(key2) + 1
    return index1 * index2
