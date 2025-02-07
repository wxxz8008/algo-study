'''
잡을 수 있는 동물의 수 출력

각 사대 기준으로 모든 동물을 탐색하면
O(m * n) = O(100_000 ** 2) => 시간초과
다른 탐색 방법을 찾아야 함

동물을 x좌표 기준으로 정렬하고,
해당 x좌표를 타겟으로 하여 가장 가까운 사대를 "이분탐색"으로 찾기
'''
from bisect import bisect_left
import sys
input = sys.stdin.readline

m, n, l = map(int, input().split()) # m: 사대의 수 / n: 동물의 수 / l: 사정거리
guns = sorted(list(map(int, input().split())))
animals = []
for _ in range(n):
    animals.append(list(map(int, input().split())))
animals = sorted(animals) 

ans = 0
for ax, ay in animals: # animal_x, animal_y
    '''
    if ay > l:
        continue
    '''
    i = bisect_left(guns, ax) # 가장 가까운 사대 찾기 => 인덱스 기준으로 들어가니까, 그 위치가 가장 가까운 사대의 위치가 됨
                                # 하지만 그 왼쪽 것이 더 가까울 수도 있으므로 i- 1도 점검
    for idx in [i - 1, i]:
        if 0 <= idx < len(guns):
            if abs(guns[idx] - ax) + ay <= l:
                ans += 1
                break

print(ans)

'''
# review
이분탐색 너무 어렵다,,,
bisect_left라도 잘 활용해보기
'''
