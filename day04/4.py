with open('day04/input.txt', 'r') as file:
    input = [list(line.strip()) for line in file]


def solution1(grid):
    word = 'XMAS'
    word_length = len(word)
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
    rows, cols = len(grid), len(grid[0])

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def find_word(x, y, dx, dy):
        return all(is_valid(x + i * dx, y + i * dy) and grid[x + i * dx][y + i * dy] == word[i] for i in range(word_length))

    return sum(1 for x in range(rows) for y in range(cols) for dx, dy in directions if find_word(x, y, dx, dy))


def solution2(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            diagonal1 = grid[y-1][x-1] + grid[y][x] + grid[y+1][x+1]
            diagonal2 = grid[y+1][x-1] + grid[y][x] + grid[y-1][x+1]
            if diagonal1 in {"MAS", "SAM"} and diagonal2 in {"MAS", "SAM"}:
                count += 1
    return count


print(solution1(input))
print(solution2(input))