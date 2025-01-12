'''
bfs, dfs 모두 가능한 문제
'''
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = True # 방문 체크
    dq = deque()
    dq.append((x, y))
    while dq:
        x, y = dq.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    dq.append((nx, ny))
                    visited[nx][ny] = True

T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split()) # k: 배추의 개수
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1 # 배추 위치 기록

    areaCnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]: # 배추 && 방문하지 않은 곳
                bfs(i, j)
                areaCnt += 1
    print(areaCnt)
