'''
산술평균
중앙값
최빈값
범위
'''
from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
li = []
ans = [0] * 4
d = defaultdict(int)

for _ in range(n):
    num = int(input())
    li.append(num)
    d[num] += 1

li.sort()
ans[0] = round(sum(li) / n) # 평균
ans[1] = li[n // 2]
ans[3] = li[-1] - li[0]

maxValue = max(d.values())
mode = []
for key in d:
    if d[key] == maxValue:
        mode.append(key)
mode.sort()
if len(mode) >= 2:
    ans[2] = mode[1]
else:
    ans[2] = mode[0]

for i in ans:
    print(i)
