'''
n개 중 m개 고르기
같은 수 중복 가능 => 단, 중복되는 수열은 출력 X
오름차순으로 출력
'''
from collections import defaultdict

dd = defaultdict(int)
n, m = map(int, input().split())
li = sorted(list(map(int, input().split())))

def func(start, part):
    global n, m
    if len(part) == m:
        if dd[tuple(part)] == 0:
            dd[tuple(part)] += 1
            print(*part)
        return

    for i in range(start, n):
        num = li[i]
        func(i, part + [num])

func(0, [])

'''
# review
list는 mutable 객체이기 때문에 dict의 key로 사용할 수 없음
반면에, tuple은 immutable 객체이기 때문에 key의 고유 해시값을 유지할 수 있어 key로 사용 가능
int로 구성된 tuple 자체를 key로 쓰고 싶을 땐,
`dd = defaultdict(int)`로 선언하면 됨
'''
