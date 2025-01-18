'''
1: 이동 O
0: 이동 X
(1, 1) -> (N, M) 지나야 하는 최소 칸 수

최소 칸, 최단 거리 문제이므로, bfs 탐색을 통해 가장 먼저 결과가 나오기만 하면 된다.
visited[][]를 활용하되, boolean이 아닌 int로 방문체크 + 거리 계산 동시에 할 수 있겠다.
=> 이 문제에선 가능하겠지만, 예전에 visited[][], dist[][]를 따로 둬야하는 문제도 있었음
'''
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def bfs(i, j):
    visited[i][j] = 1 # 방문 체크
    dq = deque([(i, j)])
    while dq:
        x, y = dq.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '1' and not visited[nx][ny]:
                    dq.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == '1' and not visited[i][j]:
            bfs(i, j)

print(visited[-1][-1])
