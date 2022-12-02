set -x

_dir="day$@"
if [ -f $_dir/__main__.py ]; then
	echo "Directory '$_dir' already initialized" >2
	exit 0
fi

mkdir -p $_dir
touch $_dir/__init__.py $_dir/input.txt
cat <<EOF > $_dir/__main__.py
from pathlib import Path


with open(Path(__file__).parent.joinpath("input.txt")) as f:
	data = f.read()

part1 = None
part2 = None

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

EOF

read -p "Paste input data into '$_day/input.txt' and then press enter"

git add $_dir
git commit -m "Creating $_dir from template"

