def get_start_of_packet_end(line: str, unique_count=4) -> int:
    for i in range(0, len(line) - unique_count):
        unique_letters = set(line[i:i+unique_count])
        if len(unique_letters) == unique_count:
            break
    return i + unique_count
