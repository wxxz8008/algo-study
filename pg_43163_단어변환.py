from collections import deque

def diff_counter(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    dq = deque()
    dq.append((begin, 0))
    while dq:
        new_word, cnt = dq.popleft()
        if target == new_word:
            return cnt
        
        for word in words:
            result = diff_counter(new_word, word)
            if result == 1:
                dq.append((word, cnt + 1))
