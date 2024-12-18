with open("day08/input.txt", "r") as file:
    grid = file.read().strip().split()


def get_locations(grid):
    locations = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            char = grid[row][col]
            if char != '.':
                if char not in locations:
                    locations[char] = []
                locations[char].append((row, col))
    return locations


def solution1(grid):
    locations = get_locations(grid)
    antinodes = set()

    for char_positions in locations.values():
        for i in range(len(char_positions)):
            for j in range(i + 1, len(char_positions)):
                x1, y1 = char_positions[i]
                x2, y2 = char_positions[j]
                row_diff, col_diff = x1 - x2, y1 - y2
                new_positions = [
                    (x1 + row_diff, y1 + col_diff),
                    (x2 - row_diff, y2 - col_diff)
                ]
                for new_row, new_col in new_positions:
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                        antinodes.add((new_row, new_col))

    return len(antinodes)


def solution2(grid):
    locations = get_locations(grid)
    antinodes = set()

    for char_positions in locations.values():
        for i in range(len(char_positions)):
            for j in range(i + 1, len(char_positions)):
                x1, y1 = char_positions[i]
                x2, y2 = char_positions[j]
                row_diff, col_diff = x1 - x2, y1 - y2

                row, col = x1, y1
                while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                    antinodes.add((row, col))
                    row += row_diff
                    col += col_diff

                row, col = x2, y2
                while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                    antinodes.add((row, col))
                    row -= row_diff
                    col -= col_diff

    return len(antinodes)


print(solution1(grid))
print(solution2(grid))