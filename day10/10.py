with open('day10/input.txt', 'r') as file:
    input = [list(map(int, line.strip())) for line in file]

def explore_trails(grid, row, col, use_visited):
    rows, cols = len(grid), len(grid[0])
    queue = [(row, col)]
    v = set()
    d = set()
    total_trails = 0

    while queue:
        r, c = queue.pop(0)

        if use_visited and (r, c) in v:
            continue
        if use_visited:
            v.add((r, c))

        if grid[r][c] == 9:
            d.add((r, c))
            total_trails += 1
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols 
                and grid[nr][nc] == grid[r][c] + 1 
                and (not use_visited or (nr, nc) not in v)):
                queue.append((nr, nc))

    return d, total_trails

def calculate_score(grid, use_visited):
    total_score = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                if use_visited:
                    d, _ = explore_trails(grid, r, c, use_visited=True)
                    total_score += len(d)
                else:
                    _, total_trails = explore_trails(grid, r, c, use_visited=False)
                    total_score += total_trails
    return total_score

def solution1(grid):
    return calculate_score(grid, use_visited=True)

def solution2(grid):
    return calculate_score(grid, use_visited=False)

print(solution1(input))
print(solution2(input))