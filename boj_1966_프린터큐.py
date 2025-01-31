'''
우선순위 큐
중요도 높은 순서대로 큐에서 pop

입력)
문서의 수, 타겟 문서의 인덱스(몇 번쨰 인쇄인지 알아내려고 하는 문서의 인덱스)

(idx, val)의 쌍을 queue에 넣는다.
'''
from collections import deque

T = int(input())
for _ in range(T):
    n, m = map(int, input().split()) # n: 문서의 수 / m: 타겟 문서의 인덱스
    li = list(map(int, input().split()))
    dq = deque(li.copy())
    li = deque(sorted(li, reverse=True)) # max 추출 대상 덱
    for idx in range(len(dq)):
        dq[idx] = (idx, dq[idx])

    # 탐색 시작
    ans = 0
    while dq:
        idx, val = dq.popleft()
        if max(li) == val: # 가장 큰 값이라면
            ans += 1
            li.popleft()
            # 근데 그게 타겟 문서의 인덱스라면
            if idx == m:
                break
        dq.append((idx, val))
    print(ans)
