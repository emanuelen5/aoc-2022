_day="day$@"

if [ -f $_day/test.py ]; then
    PYTHONPATH=$_day python3 $_day/test.py
fi

python3 -m day$@
