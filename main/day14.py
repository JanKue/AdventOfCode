import numpy as np


def main():

    file = open("../inputs/day14.txt")
    lines = file.read().splitlines()
    # print(lines)
    cave_map = build_grid(lines)
    print("Calculating ...")
    cave_map, drop_counter = drop_sand(cave_map)
    print(drop_counter)


def drop_sand(grid):
    start_point = np.array((200, 0))
    sand_pos = start_point.copy()
    counter = 0
    # while sand_pos[1] != 169:  # part 1
    while grid[tuple(start_point)] == 0:  # part 2
        if grid[sand_pos[0], sand_pos[1]+1] == 0:
            sand_pos[1] += 1
        elif grid[sand_pos[0]-1, sand_pos[1]+1] == 0:
            sand_pos[0] -= 1
            sand_pos[1] += 1
        elif grid[sand_pos[0]+1, sand_pos[1]+1] == 0:
            sand_pos[0] += 1
            sand_pos[1] += 1
        else:
            grid[tuple(sand_pos)] = 1
            sand_pos = start_point.copy()
            counter += 1
    return grid, counter


def build_grid(lines):
    grid = np.zeros((400, 170), dtype=int)
    grid[:, 169] = 10
    coordinates = [[np.array(pair.split(',')).astype(int) for pair in line.split(' -> ')] for line in lines]
    # print(coordinates)
    for structure in coordinates:
        # print(structure)
        for i in range(len(structure) - 1):
            point_a = (structure[i][0] - 300, structure[i][1])
            point_b = (structure[i+1][0] - 300, structure[i+1][1])
            a0, b0, a1, b1 = make_line_slice(point_a, point_b)
            grid[a0:b0, a1:b1] = 9
    return grid


def make_line_slice(point_a, point_b):
    min_x = min(point_a[0], point_b[0])
    max_x = max(point_a[0], point_b[0]) + 1
    min_y = min(point_a[1], point_b[1])
    max_y = max(point_a[1], point_b[1]) + 1
    return min_x, max_x, min_y, max_y


if __name__ == "__main__":
    main()
