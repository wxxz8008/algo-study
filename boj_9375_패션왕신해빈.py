'''
모든 조합의 수를 구하는 문제
T = 100
n(의상의 수) = 30
'''

T = int(input())
for _ in range(T):
    n = int(input())
    d = dict()
    for _ in range(n):
        thing, type = input().split()
        if type in d: # key in dictionary
            d[type] += 1
        else:
            d[type] = 1
    keys = list(d.keys())
    # 각 수를 그냥 곱하면 len(keys)를 모두 입어야 함
    # 안 입는다는 경우를 위해 1씩 더하고, 모든 것을 안입는 알몸 상태 1을 빼면 됨
    ans = 1
    for key in keys:
        ans *= (d[key] + 1)
    print(ans - 1)
