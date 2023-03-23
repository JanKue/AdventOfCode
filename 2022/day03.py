def main():

    file = open("inputs/day03.txt")
    lines = file.read().splitlines()
    print(lines)

    print("PART ONE")
    bad_items = [eval_rucksack(line) for line in lines]
    print(bad_items)

    priorities = [priority(item) for item in bad_items]
    print(priorities)
    print(sum(priorities))

    print("PART TWO")
    # split lines into groups of three
    thirdlen = len(lines)//3
    groups = ['']*thirdlen
    for i in range(thirdlen):
        groups[i] = lines[3*i:3*(i+1)]
    print(groups)

    badges = [eval_group(group) for group in groups]
    print(badges)

    badge_priorities = [priority(badge) for badge in badges]
    print(badge_priorities)
    print(sum(badge_priorities))


def eval_rucksack(contents):
    # split rucksack into halves
    halflen = len(contents)//2
    first_half = contents[:halflen]
    second_half = contents[halflen:]

    # check for shared items
    shared_items = list(set(first_half) & set(second_half))
    return shared_items[0]


def eval_group(group):
    # group is a list of three lines
    shared_items = list(set(group[0]) & set(group[1]) & set(group[2]))
    return shared_items[0]


def priority(letter):
    lord = ord(letter)
    prio = 0
    if 65 <= lord <= 90:
        prio = lord - 38
    elif 97 <= lord <= 122:
        prio = lord - 96
    return prio


if __name__ == "__main__":
    main()
