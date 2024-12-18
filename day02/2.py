with open('day02/input.txt') as file:
    reports = [list(map(int, line.split())) for line in file]


def valid_trend(report, min_diff, max_diff):
    return all(min_diff <= report[i + 1] - report[i] <= max_diff for i in range(len(report) - 1))

def valid_report(report):
    return valid_trend(report, 1, 3) or valid_trend(report, -3, -1)

def adjust_report(report):
    return any(valid_report(report[:i] + report[i+1:]) for i in range(len(report)))


def solution1(reports):
    return sum(1 for report in reports if valid_report(report))

def solution2(reports):
    return sum(1 for report in reports if valid_report(report) or adjust_report(report))


print(solution1(reports))
print(solution2(reports))