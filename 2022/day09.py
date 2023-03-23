from typing import Dict, Tuple

import numpy as np


def main():
    file = open("inputs/day09.txt")
    lines = file.read().splitlines()
    print(lines)

    example_instructions = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]
    example_instructions_long = ["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"]

    print("PART ONE")
    short_rope_sim = RopeSimulation(2)
    short_rope_sim.follow_instructions(lines)
    print(short_rope_sim.sections)
    print(len(short_rope_sim.tail_visited))

    print("PART TWO")
    long_rope_sim = RopeSimulation(10)
    long_rope_sim.follow_instructions(lines)
    print(long_rope_sim.sections)
    print(len(long_rope_sim.tail_visited))


class RopeSimulation:

    direction_dict = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

    def __init__(self, num_sections):
        self.sections = num_sections*[(0, 0)]
        self.tail_visited = {self.sections[num_sections - 1]}

    def follow_instructions(self, instructions: list):
        for instruction in instructions:
            direction, number = instruction.split()
            for i in range(int(number)):
                self.move_head(direction)

    def move_head(self, direction: str):
        move = self.direction_dict[direction]
        self.sections[0] = (self.sections[0][0] + move[0], self.sections[0][1] + move[1])
        for i in range(1, len(self.sections)):
            if not sections_touching(self.sections[i-1], self.sections[i]):
                self.sections[i] = move_tail_section(self.sections[i], self.sections[i-1])

        self.tail_visited.add(self.sections[-1])


def sections_touching(first, second):
    return abs(first[0] - second[0]) <= 1 and abs(first[1] - second[1]) <= 1


def move_tail_section(section, prev_section):
    new_x = section[0]
    new_y = section[1]
    x_diff = new_x - prev_section[0]
    y_diff = new_y - prev_section[1]
    if x_diff < 0:
        new_x += 1
    elif x_diff > 0:
        new_x -= 1
    if y_diff < 0:
        new_y += 1
    elif y_diff > 0:
        new_y -= 1

    return new_x, new_y


if __name__ == "__main__":
    main()
