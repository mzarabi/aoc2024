from functools import reduce
from operator import mul

def parse_input(file_path):
    positions = []
    velocities = []
    with open(file_path, "r") as file:
        for line in file.read().strip().split("\n"):
            p, v = line.split(" ")
            pos = tuple(map(int, p[2:].split(",")))
            velo = tuple(map(int, v[2:].split(",")))
            positions.append(pos)
            velocities.append(velo)
    return positions, velocities

positions, velocities = parse_input("day14/input.txt")

width = 101
height = 103

def move_robot(position, velocity, time):
    x, y = position
    vx, vy = velocity
    return ((x + time * vx) % width, (y + time * vy) % height)

def has_consecutive_positions(positions, count):
    position_set = set(positions)
    for row in set(pos[1] for pos in positions):
        consecutive_count = 0
        min_x = min(pos[0] for pos in positions if pos[1] == row)
        max_x = max(pos[0] for pos in positions if pos[1] == row)
        for column in range(min_x, max_x + 1):
            if (column, row) in position_set:
                consecutive_count += 1
                if consecutive_count >= count:
                    return True
            else:
                consecutive_count = 0
    return False

def solution1():
    quads = [0, 0, 0, 0]
    for (x, y), (vx, vy) in zip(positions, velocities):
        x, y = move_robot((x, y), (vx, vy), 100)
        if x == width // 2 or y == height // 2:
            continue
        quad_idx = (x >= width // 2) + 2 * (y >= height // 2)
        quads[quad_idx] += 1
    return reduce(mul, quads)

def solution2():
    time = 0
    while True:
        new_positions = set()
        time += 1
        for (x, y), (vx, vy) in zip(positions, velocities):
            x, y = move_robot((x, y), (vx, vy), time)
            if (x, y) in new_positions:
                break
            new_positions.add((x, y))
        if has_consecutive_positions(new_positions, 5):
            return time

print(solution1())
print(solution2())