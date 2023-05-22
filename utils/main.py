from utils.function import load_operations, get_last, sorting_operations, change_date, card_number_masking


def main():
    data = load_operations
    # last_five_operations = get_last(data)
    # sorting = sorting_operations(last_five_operations)
    # for i in sorting:
    #     from_card = change_date(i["date"])
    #     name_trans = i['description']
    #     try:
    #         name_bank = card_number_masking(i["from"])
    #     except KeyError:
    #         name_bank = "no information"
    #
    #     print(from_card, name_trans, name_bank)
    return data#, last_five_operations, get_last, sorting_operations, change_date, card_number_masking

if __name__ == '__main__':
    main()
