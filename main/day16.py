import re
import numpy as np
from collections import deque


def main():

    file = open("../inputs/day16.txt")
    lines = file.read().splitlines()

    graph, capacities = make_graph(lines)
    print(graph)
    print(capacities)
    distance_matrix = make_distance_matrix(graph)
    print(distance_matrix)


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
        capacities[name] = capacity
    return graph, capacities


def make_distance_matrix(graph):
    sorted_vertices = sorted(graph)
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
