from pathlib import Path


energies = []
with open(Path(__file__).parent.joinpath("input.txt")) as f:
    energy_sum = 0
    for line in f.readlines():
        try:
            energy_sum += int(line)
        except ValueError:
            energies.append(energy_sum)
            energy_sum = 0

print(f"Part 1: Max energy: {max(energies)}")
print(f"Part 2: Energy sum: {sum(sorted(energies)[-3:])}")
