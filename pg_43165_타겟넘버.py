answer = 0

def go(numbers, idx, val, target):
    global answer
    
    if idx == len(numbers):
        if val == target:
            answer += 1
        return
    
    go(numbers, idx + 1, val + numbers[idx], target)
    go(numbers, idx + 1, val - numbers[idx], target)
    
def solution(numbers, target):
    global answer
    
    go(numbers, 0, 0, target)
    
    return answer
