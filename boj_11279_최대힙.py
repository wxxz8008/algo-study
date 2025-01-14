'''
Python은 최소힙이 default

x가
if 자연수: 추가
elif 0: 가장 큰 값을 출력하고 제거 (== pop)
배열이 비어 있으면 0 출력
'''
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

hq = []
n = int(input())
for _ in range(n):
    x = int(input())
    # x가 자연수
    if x != 0:
        heappush(hq, -1 * x)
        continue
    # x가 0
    if len(hq) == 0:
        print(0)
    else:
        print(-1 * heappop(hq))
