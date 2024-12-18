def input_lists(filename='day01/input.txt'):
    with open(filename) as file:
        list1, list2 = zip(*(map(int, line.split()) for line in file))
    return list(list1), list(list2)


def solution1():
    list1, list2 = input_lists()
    list1.sort()
    list2.sort()
    
    return sum(abs(l1 - l2) for l1, l2 in zip(list1, list2))


def solution2():
    list1, list2 = input_lists()
    return sum(number * list2.count(number) for number in list1)


print(solution1())
print(solution2())