def main():
    # parsing data
    file = open("./inputs/day03.txt")
    grid = file.read().splitlines()

    dots = '.' * len(grid[0])
    grid.insert(0, dots)
    grid.append(dots)
    grid = ['.' + line + '.' for line in grid]

    length = len(grid)
    width = len(grid[0])

    part_num = ''
    part_num_sum = 0
    is_part = False

    has_gear = False
    gears = dict()
    gear_line, gear_col = 0, 0
    gear_ratio_sum = 0

    for i in range(length):
        for j in range(width):
            if grid[i][j].isdigit():
                part_num += grid[i][j]
                is_part = check_is_part(grid, i, j) if not is_part else is_part
                if not has_gear:
                    gear_line, gear_col = check_gear_adjacent(grid, i, j)
                has_gear = gear_line != -100
            else:
                if is_part:
                    part_num_sum += int(part_num)
                if has_gear:
                    gi = gear_line * width + gear_col
                    if gi in gears:
                        gears[gi].append(part_num)
                    else:
                        gears[gi] = [part_num]
                part_num = ''
                is_part = False
                has_gear = False

    print("Part 1:", part_num_sum)

    for gear_values in gears.values():
        if len(gear_values) == 2:
            gear_ratio = int(gear_values[0]) * int(gear_values[1])
            gear_ratio_sum += gear_ratio

    print("Part 2:", gear_ratio_sum)


def check_is_part(grid, line, col):
    up = line - 1
    down = line + 1
    left = col - 1
    right = col + 1

    neighbours = {grid[up][left], grid[up][col], grid[up][right],
                  grid[line][left], grid[line][right],
                  grid[down][left], grid[down][col], grid[down][right]}

    symbols = {'#', '$', '&', '/', '*', '+', '-', '@', '=', '?', '%'}

    return len(neighbours & symbols) != 0


def check_gear_adjacent(grid, line, col):
    up = line - 1
    down = line + 1
    left = col - 1
    right = col + 1

    if grid[up][left] == '*':
        return up, left
    if grid[up][col] == '*':
        return up, col
    if grid[up][right] == '*':
        return up, right

    if grid[line][left] == '*':
        return line, left
    if grid[line][right] == '*':
        return line, right

    if grid[down][left] == '*':
        return down, left
    if grid[down][col] == '*':
        return down, col
    if grid[down][right] == '*':
        return down, right

    return -100, -100


if __name__ == '__main__':
    main()