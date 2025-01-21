'''
재귀 or dp
0과 1이 각각 몇 번 호출되는지 고르는 문제
'''

# 1. 재귀
'''
def go(n):
    global zero, one
    if n == 0:
        zero += 1
        return 0
    elif n == 1:
        one += 1
        return 1
    return go(n - 1) + go(n - 2)

t = int(input())
for _ in range(t):
    zero, one = 0, 0
    n = int(input())
    go(n)
    print(zero, one)
'''

'''
재귀로 구현했을 시 시간초과 발생
0.25초면 O(1억 // 4) 정도에 통과해야 함 -> 2**40만 봐도 불가능
=> 재귀가 아니라면 dp밖에 없다는 결론.

직접 쓰며 규칙을 찾아보면, zero와 one을 각각의 배열로 모았다고 가정했을 때
zero[n] = one[n-1]
one[n] = zero[n-1] + one[n-1]
위와 같은 점화식을 찾을 수 있음
'''

# 2. dp
t = int(input())

dp = [[0, 0] for _ in range(41)] # [zero, one]
dp[0] = [1, 0]
for i in range(1, 41):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][1]

for _ in  range(t):
    n = int(input())
    print(*dp[n])
