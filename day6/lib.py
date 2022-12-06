def get_start_of_packet_end(line: str) -> int:
    for i in range(0, len(line) - 4):
        unique_letters = set(line[i:i+4])
        if len(unique_letters) == 4:
            break
    return i + 4
