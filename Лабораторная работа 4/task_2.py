import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    """
    Конвертер из CSV в JSON формат

    Функция считывающая данные из CSV-файла, преобразуя их в список словарей и сохраняя данные в файле JSON.
    """
    with open(INPUT_FILENAME, "r", encoding="utf-8") as input_file:
        reader = csv.DictReader(input_file, delimiter=",", quotechar="\n")
        list_data = [row for row in reader]

    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output_file:
        json.dump(list_data, output_file, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
