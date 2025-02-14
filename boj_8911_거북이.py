'''
F: 앞으로
B: 뒤로
L: 왼 90 회전
R: 오 90 회전

(max(x) - min(x)) * (max(y) - min(y))
'''
import sys
input = sys.stdin.readline

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 북 동 남 서

T = int(input())
for _ in range(T):
    orders = input().rstrip()
    dir = 0
    x, y = 0, 0
    x_list, y_list = [0], [0]

    for order in orders:
        if order == 'L':
            dir -= 1
        elif order == 'R':
            dir += 1
        elif order == 'F':
            x += dirs[dir % 4][0]
            y += dirs[dir % 4][1]
        elif order == 'B':
            x -= dirs[dir % 4][0]
            y -= dirs[dir % 4][1]
        x_list.append(x)
        y_list.append(y)

    ans = (max(x_list) - min(x_list)) * (max(y_list) - min(y_list))
    print(ans)
