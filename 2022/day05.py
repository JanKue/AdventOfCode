from collections import deque

def main():

    file = open("inputs/day05.txt")
    data = file.read()
    sections = data.split('\n\n')
    starting_config = sections[0]
    instructions = sections[1].splitlines()
    print(starting_config)
    print(instructions)

    print("PART ONE")
    stacks = setup_stacks(starting_config)
    print(stacks)

    for i in instructions:
        o_index, t_index, number = parse_instruction(i)
        move_items_single(stacks[o_index], stacks[t_index], number)

    final_tops = top_items(stacks)
    print(final_tops)

    print("PART TWO")
    stacks = setup_stacks(starting_config)
    print(stacks)

    for i in instructions:
        o_index, t_index, number = parse_instruction(i)
        move_items_multiple(stacks[o_index], stacks[t_index], number)

    final_tops = top_items(stacks)
    print(final_tops)


def setup_stacks(config):
    stacks = []
    lines = config.splitlines()
    lines.reverse()
    for i in range(1, 34, 4):
        new_stack = deque()
        for line in lines:
            if line[i].isalpha():
                new_stack.append(line[i])
        stacks.append(new_stack)
    return stacks


def parse_instruction(instruction):
    words = instruction.split(' ')
    number = int(words[1])
    origin_index = int(words[3]) - 1
    target_index = int(words[5]) - 1

    return origin_index, target_index, number


def move_items_single(origin: deque, target: deque, number):
    for i in range(number):
        target.append(origin.pop())
    return


def move_items_multiple(origin: deque, target: deque, number):
    origin_copy = origin.copy()
    items = []
    for i in range(number):
        items.append(origin_copy[-number+i])
        origin.pop()
    target.extend(items)


def top_items(stacks):
    tops = ''
    for stack in stacks:
        tops += stack[-1]
    return tops


if __name__ == "__main__":
    main()
