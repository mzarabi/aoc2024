from functools import cmp_to_key

with open('day05/rules.txt', 'r') as file:
    rules = [rule.strip().split('|') for rule in file if '|' in rule.strip()]

with open('day05/input.txt', 'r') as file:
    lines = [line.strip().split(',') for line in file if line.strip()]


def solution1():
    total = 0
    for line in lines:
        for rule in rules:
            if rule[0] in line and rule[1] in line and line.index(rule[0]) > line.index(rule[1]):
                break
        else:
            total += int(line[len(line) // 2])
    return total

def solution2():
    total = 0
    for line in lines:
        line_sorted = sorted(line, key=cmp_to_key(mycmp))
        if line != line_sorted:
            total += int(line_sorted[len(line) // 2])
    return total

def mycmp(a, b):
    for r in rules:
        if (r[0], r[1]) == (a, b):
            return -1
        if (r[1], r[0]) == (a, b):
            return 1
    return 0


print(solution1())
print(solution2())