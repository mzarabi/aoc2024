from itertools import product

with open("day07/input.txt", "r") as file:
    totals, numbers = [], []

    for line in file:
        total, number = line.strip().split(":")
        totals.append(int(total.strip()))
        numbers.append(list(map(int, number.split())))
totals, numbers = totals, numbers


def evaluate(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
        elif operators[i] == "||":
            result = int(str(result) + str(numbers[i + 1]))
    return result


def solution(operators):
    total_sum = 0
    for target, nums in zip(totals, numbers):
        possible_operators = product(operators, repeat=len(nums) - 1)
        for operator in possible_operators:
            if evaluate(nums, operator) == target:
                total_sum += target
                break
    return total_sum


print(solution(["+", "*"]))
print(solution(["+", "*", "||"]))