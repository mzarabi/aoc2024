with open("day06/input.txt", "r") as file:
    grid = file.read().strip().split()

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def patrol(obstruction, start_pos, start_dir, track_states):
    visited_pos = set()
    r, c = start_pos
    current_direction = start_dir
    rows, cols = len(grid), len(grid[0])

    while True:
        state = (r, c, current_direction)
        if track_states and state in visited_pos:
            return True
        visited_pos.add(state if track_states else (r, c))

        dr, dc = DIRECTIONS[current_direction]
        next_r, next_c = r + dr, c + dc

        if not (0 <= next_r < rows and 0 <= next_c < cols):
            return visited_pos if not track_states else False

        if grid[next_r][next_c] == '#' or (obstruction == (next_r, next_c)):
            current_direction = (current_direction + 1) % 4
        else:
            r, c = next_r, next_c


def solution1(grid):
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                row, col = i, j

    direction_index = 0
    visited = set([(row, col)])

    while True:
        new_row = row + DIRECTIONS[direction_index][0]
        new_col = col + DIRECTIONS[direction_index][1]
        if new_row not in range(rows) or new_col not in range(cols):
            break
        if grid[new_row][new_col] == '#':
            direction_index = (direction_index + 1) % 4
        else:
            row, col = new_row, new_col
            visited.add((row, col))

    return len(visited)


def solution2():
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                row, col = i, j

    positions = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and (r, c) != (row, col):
                if patrol((r, c), (row, col), 0, True):
                    positions.append((r, c))

    return len(positions)


print(solution1(grid))
print(solution2())
