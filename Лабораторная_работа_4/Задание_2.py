# TODO импортировать необходимые молули
import json
from csv import DictReader

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    res = []
    with open(INPUT_FILENAME, 'r', newline="") as csv_file:
        reader = DictReader(csv_file)
        for row in reader:
            res.append(row)

    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(obj=res, fp=json_file, indent=4)

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")


