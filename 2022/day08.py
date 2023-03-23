import numpy as np


def main():
    file = open("inputs/day08.txt")
    lines = file.read().splitlines()

    grid = [[int(char) for char in line] for line in lines]
    grid = np.array(grid)
    print(grid)

    example_grid = np.array([[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]])

    visible = find_visible(grid)
    print(visible)

    scenic_scores = viewing_distances(grid)
    print(scenic_scores)
    print(np.max(scenic_scores))


def viewing_distances(grid: np.ndarray):
    results = np.zeros(shape=grid.shape, dtype=grid.dtype)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            current_item = grid[i, j]
            # looking left
            left_score = 0
            for left_item in np.flip(grid[i, :j]):
                left_score += 1
                if left_item >= current_item:
                    break
            # looking above
            above_score = 0
            for above_item in np.flip(grid[:i, j]):
                above_score += 1
                if above_item >= current_item:
                    break
            # looking right
            right_score = 0
            for right_item in grid[i, j + 1:]:
                right_score += 1
                if right_item >= current_item:
                    break
            # looking below
            below_score = 0
            for below_item in grid[i + 1:, j]:
                below_score += 1
                if below_item >= current_item:
                    break
            results[i, j] = left_score * above_score * right_score * below_score

    return results


def find_visible(grid: np.ndarray):
    # an item is visible if it is larger than all items between itself and an edge
    # all edge items are visible to start
    visible_num = 2 * grid.shape[0] + 2 * (grid.shape[1] - 2)

    # now only check the inner items
    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            if grid[i, j] > max(grid[:i, j]) or grid[i, j] > max(grid[i, :j]) \
                    or grid[i, j] > max(grid[i + 1:, j]) or grid[i, j] > max(grid[i, j + 1:]):
                visible_num += 1

    return visible_num


if __name__ == "__main__":
    main()
