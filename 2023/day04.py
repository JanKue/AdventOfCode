import re


def main():
    # parsing data
    file = open("./inputs/day04.txt")
    lines = file.read().splitlines()

    card_copies = dict()
    for i in range(len(lines)):
        card_copies[i+1] = 1
    card_value_sum = 0

    for card in lines:
        card_id_str, nums = card.split(':')
        win_nums, my_nums = nums.split('|')
        win_nums, my_nums = int_list(win_nums), int_list(my_nums)
        intersect = set(win_nums) & set(my_nums)
        win_count = len(intersect)
        # part 1
        card_value = 2**(win_count - 1) if win_count > 0 else 0
        card_value_sum += card_value
        # part 2
        card_id = int(card_id_str.split(' ')[-1])
        for j in range(win_count):
            card_copies[card_id + j + 1] += card_copies[card_id]

    print("Part 1:", card_value_sum)
    card_copies_sum = sum(card_copies.values())
    print("Part 2:", card_copies_sum)


def int_list(number_string : str, sep=' '):
    string_list = number_string.split(sep=sep)
    return [int(n) for n in string_list if n.isdigit()]


if __name__ == '__main__':
    main()
