'''
DP? 혹은 완탐?
n = 50_000이니까
만약 한 개의 숫자로만 표현된다면, 223.xx ** 2
224라고 생각하면 => 224C1 + 224C2 + 224C3 + 224C4 => 시간초과

1, 4, 9, 16.. 을 '제곱원천수'(=target)라고 칭할 때,
dp[현재 수] = dp[제곱원천수] + dp[현재 수 - 제곱원천수]
라는 공식을 찾을 수 있음

=>
위의 방법이 최선이 아님
이제껏 나왔던 모든 제곱원천수의 조합 중 가장 최선을 찾아내야 함
ex) 12
-> 9 + 1 + 1 + 1 vs. 4 + 4 + 4
'''

import math
import sys

n = int(input())
dp = [0, 1]

for i in range(2, n + 1):
    minVal = sys.maxsize
    for j in range(1, int(math.sqrt(i)) + 1):
        minVal = min(minVal, dp[i - j * j])
    dp.append(minVal + 1)

print(dp[n])

'''
# review
for문을 한 번 더 돌면서 최적의 값 찾아내기
'''
