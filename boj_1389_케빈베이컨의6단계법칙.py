'''
케빈 베이컨의 수가 가장 작은 사람 찾기

A -> B: 계속해서 갈 수 있는 최소의 거리를 기록해야 하는 문제
'모든 점 -> 모든 점' 이므로
1) 다익스트라 노드마다 for문
2) 플로이드 워셜

graph[][]
visited[i][j]: i -> j로 가는 최단거리
'''
from collections import deque
import sys
minVal = sys.maxsize # 최댓값 셋팅 => 각 노드의 케빈 베이컨 수를 바로 갱신할 변수
ans = -1 # 정답 노드

n, m = map(int, input().split()) # n: 노드의 수 / m: 엣지의 수
graph = [[0] * (n + 1) for _ in range(n + 1)] # 0 padding
# visited = [[0] * (n + 1) for _ in range(n + 1)] # 0 padding
for _ in range(m):
    nodeA, nodeB = map(int, input().split())
    graph[nodeA][nodeB] = 1
    graph[nodeB][nodeA] = 1

def bfs(node):
    global ans, minVal
    visited = [0 for _ in range(n + 1)]
    dq = deque([node])
    visited[node] = 1
    while dq:
        start = dq.popleft()

        for next in range(1, n + 1):
            if not visited[next] and graph[start][next] == 1:
                visited[next] = visited[start] + 1
                dq.append(next)

    # 값 갱신
    if minVal > sum(visited):
        ans = node
        minVal = sum(visited)

for i in range(1, n + 1):
    bfs(i)

print(ans)
