from collections import defaultdict
import sys
input = sys.stdin.readline

dd = defaultdict(int)
n, m = map(int, input().split())
for _ in range(n):
    memo = input().rstrip()
    dd[memo] += 1
for _ in range(m):
    blogs = input().rstrip().split(',')
    for blog in blogs:
        if dd[blog] == 1:
            n -= 1
            dd[blog] = 0
    print(n)
