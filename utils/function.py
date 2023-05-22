import json
import os.path
from datetime import datetime

from pip._internal import operations

all_operations = os.path.join('../operations.json')


def load_operations(filename):
    """
    Вывод всех операций
    """
    with open(filename, 'r', encoding='utf-8') as file:
        operations = json.load(file)
    return operations


def get_last(operations):
    """
    выбирает из словаря 5 операций EXECUTED
    """
    last_operation = []
    for i in operations[::-1]:
        if i["state"] == "EXECUTED":
            last_operation.append(i)
            if len(last_operation) == 5:
                break
    return last_operation


def sorting_operations(operations):
    for i in range(len(operations) - 1):
        for j in range(len(operations) - i - 1):
            if operations[j]["data"] < operations[j + 1]["data"]:
                operations[j], operations[j + 1] = operations[j + 1], operations[j]
    return operations


def card_number_masking(operations):
    number = operations.split()[-1]
    if len(number) == 16:
        number_masking = number[:4] + " " + number[4:6] + "** ****" + number[-4:]
        return number_masking

    else:
        masks_number = "**" + number[-4:]
        return masks_number


def change_date(self):
    """Метод изменяет дату на нужную"""
    date_from_str = datetime.strptime(self, '%Y-%m-%dT%H:%M:%S.%f')
    return date_from_str.strftime('%d.%m.%Y')


if __name__ == '__main__':
    print(load_operations(all_operations))
    print(get_last(operations))
