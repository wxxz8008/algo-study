'''
절댓값이 가장 작은 값 출력하고 배열에서 제거 -> pop
절댓값이 가장 작은 값이 여러 개라면 가장 작은 수 제거

x가
0이라면 -> pop 동작
0이 아니라면 -> 추가
'''
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

hq = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x != 0: # 추가
        heappush(hq, (abs(x), x))
        continue
    # 삭제 후 출력 => pop
    if hq:
        print(heappop(hq)[1])
    else:
        print(0)

'''
# review
heap에 길이 2의 tuple을 원소로 가진다고 가정했을 때,
tuple[0]의 최솟값이 동일하다면 tuple[1]이 더 작은 값이 root에 위치함!
=> 사전 순 비교
'''
