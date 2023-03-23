def main():
    file = open("inputs/day07.txt")
    lines = file.read().splitlines()
    example_input = "$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 " \
                    "g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 " \
                    "d.log\n5626152 d.ext\n7214296 k".splitlines()
    example_fs_input, _ = build_fs({'/': {}}, example_input)
    example_fs_test = {'/': {'a': {'e': {'i': 584}, 'f': 29116, 'g': 2557, 'h.lst': 62596},
                             'b.txt': 14848514,
                             'c.dat': 8504156,
                             'd': {'j': 4060174, 'd.log': 8033020, 'd.ext': 5626152, 'k': 7214296}}
                       }
    if example_fs_test == example_fs_input:
        print("SUCCESS")

    file_system, _ = build_fs({'/': {}}, lines)

    print(file_system)
    print_fs(file_system)

    dir_size_list = calculate_fs_dir_values(file_system)
    dir_size_list = flatten_list(dir_size_list)

    print("PART ONE")
    small_dirs = [d for d in dir_size_list if d <= 100_000]
    print(small_dirs)
    print(sum(small_dirs))

    print("PART TWO")
    desired_size = 70_000_000 - 30_000_000
    total_size = calculate_dict_value(file_system)
    candidate_dirs = [d for d in dir_size_list if d >= total_size - desired_size]
    print(candidate_dirs)
    print(min(candidate_dirs))


def calculate_fs_dir_values(fs):
    value_list = []
    for key in fs:
        entry = fs[key]
        if isinstance(entry, dict):
            value_list.append(calculate_dict_value(entry))
            value_list.append(calculate_fs_dir_values(entry))
        # elif isinstance(entry, int):
        #     value_dict[key] += entry

    return value_list


def calculate_dict_value(input_dict):
    value = 0
    for key in input_dict:
        entry = input_dict[key]
        if isinstance(entry, int):
            value += entry
        elif isinstance(entry, dict):
            value += calculate_dict_value(entry)
    return value


def build_fs(fs, instructions, index=0):
    while index < len(instructions):
        line = instructions[index]
        index += 1
        if line == "$ cd ..":
            return fs, index
        elif line[:4] == "$ cd":
            fs[line[5:]], index = build_fs({}, instructions, index)
        elif line[:4] == "$ ls":
            continue
        elif line[0:3] == "dir":
            fs[line[4:]] = {}
        elif line.split()[0].isdigit():
            number = int(line.split()[0])
            key = line.split()[1]
            fs[key] = number
    return fs, index


def print_fs(fs, indent=''):
    for key in fs:
        entry = fs[key]
        if isinstance(entry, dict):
            print(indent + key)
            print_fs(entry, indent + '-')
        else:
            print(indent + key, entry)


def flatten_list(list_of_lists, flat_list=[]):
    if list_of_lists == []:
        return flat_list
    else:
        for item in list_of_lists:
            if type(item) == list:
                flatten_list(item)
            else:
                flat_list.append(item)

        return flat_list


if __name__ == "__main__":
    main()
