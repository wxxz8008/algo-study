'''
최대 7자리 수 => 7!
각 수에 대해 반복문을 통해 소수 찾기 => 1_000_000

O(7! * )
'''
from itertools import permutations as pm

def solution(numbers):
    
    numberList = []
    for i in pm(numbers, len(numbers)):
        print(i)
        joinNumber = int(''.join(i))
        numberList.append(joinNumber)
    
    answer = 0
    for number in numberList:
        if isPrime(number):
            answer += 1
    
    return answer

def isPrime(number):
    count = 0 
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count == 2:
        return True
    return False
    
