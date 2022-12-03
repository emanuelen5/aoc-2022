set -x

_dir="day$@"
if [ -d $_dir ]; then
    echo "Directory '$_dir' already created" >2
    exit 1
fi

_branch="day/$@"
git branch $_branch
if [ $? -ne 0 ]; then
    echo "Branch '$_branch' does already exist. Clean up first and delete it to be able to initialize" >2
    exit 1
fi
git checkout $_branch

cp -r template/ $_dir

read -p "Paste input data into '$_day/data/input.txt' and '$_day/data/test_input.txt' and then press Enter to continue... "

git add $_dir
git commit -m "Creating $_dir from template"
