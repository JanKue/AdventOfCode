def main():

    file = open("../inputs/day4.txt")
    lines = file.read().splitlines()
    print(lines)

    ranges = [line.split(',') for line in lines]
    print(ranges)

    ranges_containing = [containing(pair[0], pair[1]) for pair in ranges]
    print(ranges_containing)
    print(sum(ranges_containing))

    ranges_overlaps = [any_overlap(pair[0], pair[1]) for pair in ranges]
    print(ranges_overlaps)
    print(sum(ranges_overlaps))


def containing(range1, range2):
    set1 = range_to_incl_set(range1)
    set2 = range_to_incl_set(range2)

    return set1.issubset(set2) or set2.issubset(set1)


def any_overlap(range1, range2):
    set1 = range_to_incl_set(range1)
    set2 = range_to_incl_set(range2)

    return not set1.isdisjoint(set2)


def range_to_incl_set(range_str):
    # range_str looks like 'x-y'
    range_str_arr = range_str.split('-')
    start = int(range_str_arr[0])
    end = int(range_str_arr[1])
    range_set = set(range(start, end+1))
    return range_set


if __name__ == "__main__":
    main()
