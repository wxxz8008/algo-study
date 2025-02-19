def solution(numbers):
    answer = ''
    
    numbers = sorted(numbers, key = lambda x: str(x) * 3, reverse = True)
    answer = ''.join(map(str, numbers))
    
    if int(answer) == 0:
        answer = str(int(answer))
    
    return answer
