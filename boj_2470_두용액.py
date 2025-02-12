'''
산성 용액            /  알칼리성 용액
1 ~ 1,000,000,000   / -1,000,000,000 ~ -1
두 개를 더해서 특성값 (두 개가 같은 속성일 수도 있음)
-> 특성값을 0에 가장 가깝게 만들기

"값이 모두 다름"

완전탐색; O(100_000 * 100_000) -> 불가능
이분탐색 or 투포인터

<이분탐색>
start, end를 idx로 설정하여 탐색

start + end를 0을 기준으로 탐색
최적의 start, end 수시로 갱신
'''
import sys
input = sys.stdin.readline

n = int(input())
li = sorted(list(map(int, input().split())))
start, end = 0, len(li) - 1
ans = []
gap = sys.maxsize
while start < end:
    if li[start] + li[end] == 0:
        ans = [li[start], li[end]]
        break
    # 최적의 gap 갱신
    if gap > abs(li[start] + li[end]):
        gap = abs(li[start] + li[end])
        ans = [li[start], li[end]]
    if li[start] + li[end] > 0:
        end -= 1
    else:
        start += 1

print(*ans)
