'''
사과 -> 뱀 길이 늘어남
뱀 자기 자신 혹은 벽 -> 게임 끝

"게임이 끝날 때까지의 시간 구하기"

L - 왼쪽 90도 회전
D - 오른쪽 90도 회전

뱀 deque을 유지함과 동시에 pop한 데이터를 graph에서 지워주기?
=> graph에도 굳이 뱀의 이동 현황을 기록해야할까? 사과일 때만 비워주면 되지 않을까?

'''
from collections import deque
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동 남 서 북

n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)] # 0 == 이동 가능
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1 # 1 == 사과 <!-- 2 == 사과 -->

rotate = []
l = int(input())
for _ in range(l):
    x, c = input().rstrip().split() # x: 초 , c: 왼/오
    rotate.append((int(x), c))

# print(rotate)

sec = 0
cx, cy = 0, 0 # 현재 위치
dir = 0 # 현재 방향
snake = deque([(0, 0)])
while True:
    # sec update
    sec += 1

    # 이동할 idx 선택
    x, y = dirs[dir % 4]
    cx, cy = cx + x, cy + y

    # 이동할 위치가 벽 => break
    if 0 > cx or cx >= n or 0 > cy or cy >= n:
        break

    # 이동할 위치가 뱀 => break
    if (cx, cy) in snake:
        break

    # 사과 체크 && 이동(=꼬리 삭제)
    if graph[cx][cy] == 1:
        graph[cx][cy] = 0
    else:
        snake.pop()
    # 머리 갱신
    snake.appendleft((cx, cy))

    # rotate 벽 or 뱀  rotate.pop(0) =>  dir 방향 갱신
    if rotate and rotate[0][0] == sec:
        leftOrRight = rotate.pop(0)[1]
        if leftOrRight == 'D': # 오른쪽 90도 회전
            dir += 1
        elif leftOrRight == 'L': # 왼쪽 90도 회전
            dir -= 1

print(sec)
