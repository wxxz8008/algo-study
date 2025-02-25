
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dq = deque()
    dq.append((0, 0, 1))
    visited[0][0] = True
    
    while dq:
        x, y, cnt = dq.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx == n - 1 and ny == m - 1:
                answer.append(cnt + 1)
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                dq.append((nx, ny, cnt + 1))
    
    if not answer:
        return -1
    return min(answer)
