with open('day12/input.txt') as f:
    grid = f.read().strip().split()

def is_same(grid, i, j, plant):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return False
    return grid[i][j] == plant

def get_corners(grid, i, j):
    plant = grid[i][j]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    adjacent = [is_same(grid, i + dr, j + dc, plant) for dr, dc in directions]
    N, S, W, E, NW, NE, SW, SE = adjacent[:8]

    count = 0
    if N and W and not NW:
        count += 1
    if N and E and not NE:
        count += 1
    if S and W and not SW:
        count += 1
    if S and E and not SE:
        count += 1
    if not (N or W):
        count += 1
    if not (N or E):
        count += 1
    if not (S or W):
        count += 1
    if not (S or E):
        count += 1

    return count

def get_region(grid, start_i, start_j, visited):
    plant = grid[start_i][start_j]
    region = set()
    stack = [(start_i, start_j)]

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue

        visited.add((x, y))
        region.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == plant and (nx, ny) not in visited:
                stack.append((nx, ny))

    return region

def calculate_fence_cost(grid, region):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    fence = 0
    for x, y in region:
        plant = grid[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])) or grid[nx][ny] != plant:
                fence += 1
    return len(region) * fence

def calculate_corner_cost(grid, region):
    total_corners = sum(get_corners(grid, x, y) for x, y in region)
    return total_corners * len(region)

def solve(grid, cost_function):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_cost = 0

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                region = get_region(grid, i, j, visited)
                total_cost += cost_function(grid, region)

    return total_cost

def solution1(grid):
    return solve(grid, calculate_fence_cost)

def solution2(grid):
    return solve(grid, calculate_corner_cost)

print(solution1(grid))
print(solution2(grid))