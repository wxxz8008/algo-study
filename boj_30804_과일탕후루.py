'''
1~9: 9가지 종류의 과일
총 n개의 과일 탕후루 (n = 300_000)
=> S1.. Sn

양쪽에서 과일을 빼서 2개의 과일로만 이루어진 탕후루 만들기
=> 과일 개수가 가장 많은 탕후루의 개수 출력

1) 완전탐색

2) 투포인터
    left, right = 0, 0일 때,


'''
from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
left, right = 0, 0
maxLength = 0
typeCnt = 0
dd = defaultdict(int)

while right < n:
    # left, right에 따른 과일 개수 기록
    if dd[li[right]] == 0: # 나오지 않았던 과일 종류라면
        typeCnt += 1
    dd[li[right]] += 1
    right += 1 # 다음 while문에서 적용될 인덱스 (미리 ++ 해두기)
    while typeCnt > 2:
        dd[li[left]] -= 1
        if dd[li[left]] == 0:
            typeCnt -= 1 # 과일 종류 감소
        left += 1
    maxLength = max(maxLength, right - left)

print(maxLength)
