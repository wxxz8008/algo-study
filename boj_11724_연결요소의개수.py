'''
방향 없는 그래프
연결된 그래프의 개수 구하기
'''
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n: node, m: edge
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
cnt = 0
for _ in range(m):
    nodeA, nodeB = map(int, input().split())
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)
# 탐색 시작
for node in range(1, n + 1):
    if not visited[node]:
        cnt += 1
        visited[node] = True
        dq = deque()
        dq.append(node)
        while dq:
            nodeA = dq.popleft()
            for nodeB in graph[nodeA]:
                if not visited[nodeB]:
                    visited[nodeB] = True
                    dq.append(nodeB)
print(cnt)
