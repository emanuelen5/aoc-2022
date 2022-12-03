_day="$@"

if [ -f $_day/test.py ]; then
    PYTHONPATH=$_day python3 $_day/test.py && echo "Tests passed"
fi

python3 -m $@
