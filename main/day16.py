import re
import numpy as np
from collections import deque


def main():

    file = open("../inputs/example16.txt")
    lines = file.read().splitlines()

    graph, capacities = make_graph(lines)
    print(graph)
    print(capacities)
    print(sorted(graph))
    distance_matrix = make_distance_matrix(graph)
    print(distance_matrix)

    position = 'AA'
    total_flow = round_flow = 0

    for i in range(30):
        print(position)
        if capacities[position] > 0:
            round_flow += capacities[position]
            capacities[position] = 0
        else:
            goal = pick_best_next(graph, capacities, distance_matrix, position)
            position = move_in_direction(graph, position, goal)
        print(round_flow)
        total_flow += round_flow
    print("total")
    print(total_flow)


def move_in_direction(graph, current, goal):
    possible_moves = graph[current]
    if goal in possible_moves:
        return goal
    path = find_path(graph, current, goal)
    return path[-1]


def find_path(graph, root, goal):
    queue = deque([root])
    visited = {root}
    previous = {}
    while len(queue) > 0:
        v = queue.popleft()
        if v == goal:
            prev = v
            path = []
            while prev != root:
                path.append(prev)
                prev = previous[prev]
            return path if len(path) > 0 else ['AA']
        for t in graph[v]:
            if t not in visited:
                previous[t] = v
                queue.append(t)
                visited.add(t)
    return ['AA']


def pick_best_next(graph, capacities, distance_matrix, current):
    sorted_vertices = sorted(graph.keys())
    index = sorted_vertices.index(current)
    distances = distance_matrix[index]
    # determine ratings of other valves
    ratings = [capacities[sorted_vertices[i]] - distances[i] for i in range(len(distances))]
    # select best next valve
    selection = current
    sel_i = 0
    for i in range(len(ratings)):
        if i == index:
            continue
        elif ratings[i] > ratings[sel_i]:
            selection = sorted_vertices[i]
            sel_i = i
        elif ratings[i] == ratings[sel_i]:
            if distances[i] < distances[sel_i]:
                selection = sorted_vertices[i]
                sel_i = i

    return selection


def make_graph(lines):
    graph = {}
    capacities = {}
    for line in lines:
        re_match = re.match(
            r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? "
            r"([A-Z]{2},? ?[A-Z]{0,2},? ?[A-Z]{0,2},? ?[A-Z]{0,2},? ?[A-Z]{0,2},? ?)",
            line
        )
        name, capacity, targets = re_match.groups()
        graph[name] = targets.split(', ')
        capacities[name] = int(capacity)
    return graph, capacities


def make_distance_matrix(graph):
    sorted_vertices = sorted(graph.keys())
    matrix = np.full(fill_value=1000, shape=(len(graph), len(graph)), dtype=int)

    for i in range(matrix.shape[0]):
        queue = deque([i])
        visited = {i}
        while len(queue) > 0:
            v = queue.popleft()
            if v == i:
                matrix[i, v] = 0
            ts = np.array([sorted_vertices.index(t) for t in graph[sorted_vertices[v]]])
            for t in ts:
                if t not in visited:
                    matrix[i, t] = min(matrix[i, t], matrix[i, v] + 1)
                    queue.append(t)
                    visited.add(t)

    return matrix


if __name__ == "__main__":
    main()
