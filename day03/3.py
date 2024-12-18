import re

MATCHING_PATTERN = r"mul\((\d+),(\d+)\)"
SPLIT_PATTERN = r"(do\(\)|don't\(\))"

with open('day03/input.txt') as file:
    input_data = file.read()


def solution1(input_string):
    matches = re.findall(MATCHING_PATTERN, input_string)
    return sum(int(a) * int(b) for a, b in matches)


def solution2(input_string):
    rows = re.split(SPLIT_PATTERN, input_string)
    
    enabled = True
    total_sum = 0
    for row in rows:
        if row == "do()":
            enabled = True
        elif row == "don't()":
            enabled = False
        if enabled:
            matches = re.findall(MATCHING_PATTERN, row)
            total_sum += sum(int(a) * int(b) for a, b in matches)
    return total_sum


print(solution1(input_data))
print(solution2(input_data))