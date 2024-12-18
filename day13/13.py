from sympy import symbols, Eq, solve

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split("\n\n")

    numbers = []
    for block in lines:
        blocks = []
        for line in block.split("\n"):
            for word in line.replace(",", "").split():
                if "+" in word:
                    parts = word.split("+")
                    if parts[1].isdigit():
                        blocks.append(int(parts[1]))
                elif "=" in word:
                    parts = word.split("=")
                    if parts[1].isdigit():
                        blocks.append(int(parts[1]))
        numbers.append(blocks)
    return numbers

def calculate(numbers, add):
    x, y = symbols('x y')
    ax, ay, bx, by, rx, ry = numbers

    equations = [
        Eq(ax * x + bx * y, rx + add),
        Eq(ay * x + by * y, ry + add)
    ]

    solution = solve(equations, (x, y))

    if all(val.is_integer for val in solution.values()):
        return solution[x] * 3 + solution[y]
    return 0

def solution(numbers, add):
    return sum(calculate(num, add) for num in numbers)


numbers = parse_input('day13/input.txt')
print(solution(numbers, 0))
print(solution(numbers, 10000000000000))