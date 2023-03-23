import numpy as np
from collections import deque


def main():

    file = open("inputs/day12.txt")
    lines = file.read().splitlines()
    board = np.array([[char for char in line] for line in lines])
    heights = np.array([[char_height(char) for char in line] for line in lines])
    heights = np.pad(heights, 1, "constant", constant_values=-10)

    print(board)
    print(heights)
    start_pos = np.where(board == 'S')
    start_pos = tuple(np.array(start_pos).flatten() + [1, 1])
    print(start_pos)
    end_pos = np.where(board == 'E')
    end_pos = tuple(np.array(end_pos).flatten() + [1, 1])
    print(end_pos)

    shortest = search(heights, end_pos, start_pos)
    print(shortest)


def search(graph, root, goal):
    queue = deque([root])
    explored = set(root)
    depth = graph.copy()
    depth[root] = 0
    while len(queue) > 0:
        vertex = queue.popleft()
        if vertex == goal:
            return depth[vertex]
        for target in viable_move_targets(graph, vertex):
            if target not in explored:
                explored.add(target)
                queue.append(target)
                depth[target] = depth[vertex] + 1
    return depth


def viable_move_targets(heights, current_pos: tuple):
    current_height = heights[current_pos]
    current_pos = np.array(current_pos)
    moves = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]])
    viable_targets = []
    for move in moves:
        move_target = tuple(current_pos + move)
        move_height = heights[move_target]
        if move_height + 1 >= current_height:
            viable_targets.append(move_target)
    return viable_targets


def char_height(character):
    if character == 'S':
        return 0
    if character == 'E':
        return 25
    return ord(character) - ord('a')


if __name__ == "__main__":
    main()
