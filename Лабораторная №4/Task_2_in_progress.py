# TODO импортировать необходимые молули
import csv
import json
import tempfile

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(filepath) -> None:
    with open(filepath) as f:
        lines = [line for line in csv.DictReader(f)]
        json.dumps(lines, indent=4)
        with open('output.json', 'w') as out_f:
            json.dumps(lines, indent=4)



    # TODO считать содержимое csv файла

    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")


