import json

INPUT_FILE = "input.json"


def task() -> float:
    """
    Функция для подсчета суммы произведений двух значений в каждом словаре из JSON файла.
    """
    with open(INPUT_FILE, "r", encoding="utf-8") as input_file:
        json_data = json.load(input_file)

    sum_data = sum([item["score"] * item["weight"] for item in json_data])
    return round(sum_data, 3)


print(task())
