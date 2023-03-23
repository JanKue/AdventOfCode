import json
import functools


def main():

    file = open("inputs/day13.txt")
    data = file.read()
    example_data = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

    pairs = data.split('\n\n')
    print(pairs)
    pairs = [[json.loads(lst) for lst in pair.splitlines()] for pair in pairs]
    print(pairs)

    print("PART ONE")
    index_sum = 0
    for i in range(len(pairs)):
        if compare_lists(pairs[i][0], pairs[i][1]):
            index_sum += i + 1
    print(index_sum)

    print("PART TWO")
    packets = [packet for pair in pairs for packet in pair]
    divider_one = [[2]]
    divider_two = [[6]]
    packets.extend([divider_one, divider_two])
    sorted_packets = sorted(packets, key=functools.cmp_to_key(compare_lists_sorting))
    divider_one_pos = sorted_packets.index(divider_one) + 1
    divider_two_pos = sorted_packets.index(divider_two) + 1
    print(divider_one_pos * divider_two_pos)


def compare_lists_sorting(a, b):
    comparison = compare_lists(a, b)
    if comparison is None:
        return 0
    elif comparison:
        return -1
    else:
        return 1


def compare_lists(a, b):
    # print("comparing", a, "vs", b)
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True
        elif a > b:
            return False
        elif a == b:
            return None
        return a < b
    elif isinstance(a, list) and isinstance(b, list):
        # checking for empty lists
        if not a:
            if not b:
                return None
            return True
        if not b:
            return False
        # comparing non-empty lists
        comparison = compare_lists(a[0], b[0])
        if comparison:
            return True
        elif comparison is None:
            return compare_lists(a[1:], b[1:])
        else:
            return False
    elif isinstance(a, int) and isinstance(b, list):
        return compare_lists([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare_lists(a, [b])


if __name__ == "__main__":
    main()
