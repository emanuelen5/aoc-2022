set -x

_dir="day$@"
if [ -f $_dir/__main__.py ]; then
    echo "Directory '$_dir' already initialized" >2
    exit 0
fi

mkdir -p $_dir
touch $_dir/lib.py $_dir/input.txt
cat <<EOF > $_dir/__main__.py
from pathlib import Path
from . import lib


with open(Path(__file__).parent.joinpath("input.txt")) as f:
    data = f.read()

part1 = None
part2 = None

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
EOF

cat <<EOF > $_dir/test.py
from pathlib import Path
import unittest
import lib


with open(Path(__file__).parent.joinpath("test_input.txt"), 'r') as f:
    test_input = [line.strip for line in f.readlines()]


tc = unittest.TestCase()
EOF

read -p "Paste input data into '$_day/input.txt' and then press enter"

_branch="day/$@"
git branch $_branch
git checkout $_branch
git add $_dir
git commit -m "Creating $_dir from template"
