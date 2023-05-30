"""Импортируем функции из файла function.py"""
from function import load_operations, get_last, sorting_operations, change_date, card_number_masking


def main():
    data = load_operations()  # выгружает все операции из json файла operation.json

    last_operation = get_last(data)  # последние пять операций

    sorting = sorting_operations(last_operation)  # сортирует последние пять оперциий по дате (пузырьковый метод)
    for i in sorting:
        from_card = change_date(i['date'])  # устанавливает нужный формат даты
        name_trans = i['description']  # вывод названия операции
        try:
            from_ = card_number_masking(i['from'])
        except KeyError:
            from_ = "no information"  # если нет информации откуда, выводим "no information"
        try:
            to_ = card_number_masking(i['to'])
        except KeyError:
            to_ = "no information"  # если нет информации куда, выводим "no information"

        summ = i['operationAmount']['amount']  # вывод суммы
        valu = i['operationAmount']['currency']['name']  # вывод валюты

        print(f'{from_card} {name_trans}\n{from_} -> {to_}\n{summ} {valu}')
        print(" ")
        """
        Вывод операций в нужном формате с замаскированным счетом или номером карты
        """
    return


main()
