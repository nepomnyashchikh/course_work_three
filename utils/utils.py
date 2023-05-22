import json
import os.path

full_baza = os.path.join('../operations.json')


def load_baza(filename):
    """
    Вывод всех операций
    """
    with open(filename, 'r', encoding='utf-8') as file:
        baza = json.load(file)
    return baza


print(load_baza(full_baza))
