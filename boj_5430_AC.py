'''
새로운 언어 AC
R(뒤집기): 배열 순서 뒤집기
D(버리기): 첫 번쨰 수 버리기 -> 배열이 비어있을 때 사용하면 에러

함수 100_000번
배열 길이 100_000
배열을 계속 돌리기만 한다면 시간초과 --> 역순 정렬 시간복잡도 알아보기 !! 아마도 O(len(li))

sol)
앞뒤로 모두 뺄 수 있도록 deque을 사용하되,
뒤집는 횟수만 잘 기록해서 마지막에 역순 정렬 할지 안할지 정하기
'''
from collections import deque
import sys
input = sys.stdin.readline

def printer(li):
    # li == ['3', '2', '7']
    return_s = '['
    for i in range(len(li)):
        return_s += li[i]
        if i != len(li) - 1:
            return_s += ','
    return_s += ']'
    return return_s

T = int(input())
for _ in range(T):
    order = list(input().rstrip())
    n = int(input()) # 원소의 수

    s = input().rstrip()
    s = s[1 : len(s) - 1]
    s = s.split(',')

    if n == 0 and 'D' in order:
        print('error')
        continue

    dq = deque(s)
    reverse = 0 # 홀수면 R 동작하기
    err = False
    for o in order:
        if o == 'D': # 버리기
            if not dq:
                err = True
                break
            if reverse  % 2 == 0: # 짝수면 맨 앞 빼기
                dq.popleft()
            else:
                dq.pop()
        elif o == 'R': # 뒤집기
            reverse += 1

    if err:
        print('error')
        continue
    # 정답 출력
    dq = list(dq)
    if not dq: # 원소가 없는 경우
        print('[]')
        continue

    if reverse % 2 == 1: # 역순 출력
        print(printer(dq[::-1]))
    else:
        print(printer(dq))

'''
# review
입출력 코드가 깔끔하지 않음 

list(input().rstrip()[1 : -1].split(','))
''.join(',') 

위 두 방법을 사용했으면 더 깔끔한 코드가 됐을 것!

&&

`if not dq: # 원소가 없는 경우`
위의 코드는 굳이 필요하지 않았음
'''
