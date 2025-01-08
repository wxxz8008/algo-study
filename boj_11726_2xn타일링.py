from collections import deque

n = int(input())
dq = deque([1, 2])
cnt = 0
while True:
    cnt += 1
    ans = dq.popleft() # first
    if cnt == n:
        break
    second = dq[0]
    dq.append(ans + second)

print(ans % 10007)

'''
# review
문제를 보고 dp겠거니 했고, 직접 그려가며 규칙을 찾았지만
정확한 원리는 알지 못했음. 
'''
