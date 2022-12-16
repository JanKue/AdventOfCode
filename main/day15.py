import re
import numpy as np
from scipy.spatial.distance import cityblock


def main():

    file = open("../inputs/day15.txt")
    lines = file.read().splitlines()
    print(lines)

    sensors = [parse_coordinates(line) for line in lines]
    print(sensors)

    # checked_positions = [check_position((x, 2_000_000), sensors) for x in range(-2_000_000, 5_000_000)]
    # print(checked_positions[:20])
    # print(checked_positions[-20:])
    # print(sum(checked_positions))

    # open_position = check_all_positions(20, sensors)
    # print(open_position)
    # print(open_position[0]*4_000_000 + open_position[1])

    open_position = check_diagonal(4_000_000, sensors)
    print(open_position)
    print(open_position[0]*4_000_000 + open_position[1])


def check_diagonal(size, sensors):
    x = y = -1
    for i in range(size + 1):
        exclude_x, exclude_y = [], []
        for (sx, sy), beacon_pos, dist in sensors:
            if abs(i - sy) <= dist:
                dist_y = dist - abs(i - sy)
                exclude_y.append((max(sx - dist_y, 0), min(sx + dist_y, size)))
            if abs(i - sx) <= dist:
                dist_x = dist - abs(i - sx)
                exclude_x.append((max(sy - dist_x, 0), min(sy + dist_x, size)))
        y = max(y, find_non_excluded(exclude_x, size))
        x = max(x, find_non_excluded(exclude_y, size))
    return x, y


def find_non_excluded(intervals, ceiling):
    val = 0
    for a, b in sorted(intervals):
        if a > val:
            return val
        else:
            val = max(val, b+1)
    return val if val <= ceiling else -1


def check_all_positions(size, sensors):
    for x in range(size+1):
        y = 0
        while y < size+1:
            unblocked = True
            for (sx, sy), beacon_pos, dist in sensors:
                if cityblock((x, y), (sx, sy)) <= dist:
                    unblocked = False
                    if y - sy < 0:
                        y += 2 * abs(y - sy)
                    break
            if unblocked:
                return x, y
            y += 1
    return 0, 0


def blocked_position(coord, sensors):
    for sensor_pos, beacon_pos, dist in sensors:
        if cityblock(sensor_pos, coord) <= dist:
            return True
    return False


def check_position(coord, sensors):
    for sensor in sensors:
        sensor_pos, beacon_pos, dist = sensor
        if beacon_pos == coord:
            return 0
        elif cityblock(sensor_pos, coord) <= dist:
            return 1
    return 0


def parse_coordinates(line):

    match = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
    sx, sy, bx, by = map(int, match.groups())

    distance = cityblock((sx, sy), (bx, by))

    return (sx, sy), (bx, by), distance


if __name__ == "__main__":
    main()
