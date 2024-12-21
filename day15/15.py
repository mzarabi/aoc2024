def read_input(file_path):
    with open(file_path) as f:
        grid_input, directions_input = f.read().strip().split('\n\n', 1)
        directions = directions_input.replace('\n', '')
        grid = [list(row) for row in grid_input.split('\n')]
    return grid, directions

def find_robot(grid):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == '@':
                grid[r][c] = '.'
                return r, c
    return None, None

def move_robot(grid, robot_r, robot_c, directions):
    direction_offsets = {
        '<': (0, -1),
        '>': (0,  1),
        '^': (-1, 0),
        'v': (1,  0)
    }
    rows, cols = len(grid), len(grid[0])

    for step in directions:
        if step not in direction_offsets:
            continue

        dr, dc = direction_offsets[step]
        new_r, new_c = robot_r + dr, robot_c + dc

        while 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 'O':
            new_r += dr
            new_c += dc

        if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == '.':
            grid[new_r][new_c], grid[robot_r + dr][robot_c + dc] = (
                grid[robot_r + dr][robot_c + dc],
                grid[new_r][new_c]
            )
            robot_r += dr
            robot_c += dc

    return robot_r, robot_c

def calculate_score(grid):
    total_score = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'O':
                total_score += 100 * i + j
    return total_score

def solution1():
    grid, directions = read_input('day15/input.txt')
    robot_r, robot_c = find_robot(grid)
    move_robot(grid, robot_r, robot_c, directions)
    return calculate_score(grid)

print(solution1())