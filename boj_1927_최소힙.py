'''
파이썬에서는 최소힙이 기본

x가
자연수 -> x 추가
0 -> 가장 작은 값 출력하고 제거
'''
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

hq = []
n = int(input()) # 연산의 횟수
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heappop(hq))
    else:
        heappush(hq, x)

'''
# review
백준에서는 입력 많다 싶으면 sys.stdin.readline() 입력 사용하기 
'''
