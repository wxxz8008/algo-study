'''
- 연속된 세 개의 계단을 밟아서는 안됨
- 마지막 계단은 무조건 밟아야 함

dp) 큰 문제를 쪼개며 생각 -> 맨 뒤부터 생각해보자
'''
n = int(input())
li = [0] * 301
dp = [0] * 301
for i in range(1, n + 1):
    li[i] = int(input())

dp[1] = li[1]
dp[2] = li[1] + li[2]
dp[3] = max(li[1] + li[3], li[2] + li[3])

for i in range(4, n + 1):
    dp[i] = max(li[i] + dp[i - 2], li[i] + li[i - 1] + dp[i - 3])

print(dp[n])
