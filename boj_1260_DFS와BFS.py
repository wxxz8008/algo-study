'''
정점 번호 작은 것부터 먼저 방문
n: 정점 개수
m: 간선 개수
두 정점 사이에 여러 개의 간선이 있을 수 있음 => set 처리해야 할 듯
'''
from collections import deque

n, m, v = map(int, input().split()) # 정점, 간선, 시작 번호
graph = [[] for _ in range(n + 1)] # padding
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순 정렬
for i in range(1, n + 1):
    graph[i] = sorted(list(set(graph[i])))

visited = [False for _ in range(n + 1)] # bfs, dfs 재사용
order = []

def dfs(parent):
    order.append(parent)
    visited[parent] = True
    for child in graph[parent]:
        if not visited[child]:
            dfs(child)

def bfs(start):
    order.append(start)
    visited[start] = True
    dq = deque([start])
    while dq:
        parent = dq.popleft()
        for child in graph[parent]:
            if not visited[child]:
                dq.append(child)
                order.append(child)
                visited[child] = True

dfs(v)
print(*order)
# 갱신
visited = [False for _ in range(n + 1)] # bfs, dfs 재사용
order = []
bfs(v)
print(*order)
