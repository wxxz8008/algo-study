'''
좌표압축을 하면 나보다 작은 것의 개수와 같아야 한다
=> 결국, 나보다 작은 수의 개수를 구하라는 뜻 (단, 서로 다른 수만 세기)

n = 1_000_000
완전탐색: O(n**2) -> 시간초과

중복을 제거해야 하니까 set이 필요할 것 같고,
'''
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(list(set(nums)))

d = dict()
for idx in range(len(sorted_nums)):
    d[sorted_nums[idx]] = idx

for num in nums:
    print(d[num], end=' ')

'''
# review
set(sorted(list))은 정렬을 보장하지 않는다 == set은 원소의 순서를 보장하지 않는다
그러므로 sorted를 나중에 해야 한다.
'''
