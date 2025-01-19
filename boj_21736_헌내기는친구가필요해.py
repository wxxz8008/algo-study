'''
bfs, dfs 모두 가능

'O', 'P'(사람) 모두 이동 가능
'P'일 때만 카운트하고, 해당 값 출력하면 끝
'''
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0 # 정답

def bfs(i, j):
    global cnt
    visited[i][j] = True
    dq = deque([(i, j)])
    while dq:
        x, y = dq.popleft()
        if graph[x][y] == 'P':
            cnt += 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 'X' and not visited[nx][ny]:
                    dq.append((nx, ny))
                    visited[nx][ny] = True

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            bfs(i, j)

if cnt:
    print(cnt)
else:
    print("TT")
