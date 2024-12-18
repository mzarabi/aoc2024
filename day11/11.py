from collections import defaultdict, Counter

with open('day11/input.txt', 'r') as file:
    input = [int(num) for num in file.read().split()]


def solution(numbers, blinks):
    numbers = Counter(numbers)
    
    for _ in range(blinks):  
        newList = defaultdict(int)
        
        for num, count in numbers.items():
            if num == 0:  
                newList[1] += count  
            elif len(str(num)) % 2 == 0:  
                mid = len(str(num)) // 2
                left = int(str(num)[:mid])
                right = int(str(num)[mid:])
                newList[left] += count  
                newList[right] += count  
            else:  
                newList[num * 2024] += count  
        
        numbers = Counter(newList) 
    return sum(numbers.values()) 


print(solution(input, 25))
print(solution(input, 75))