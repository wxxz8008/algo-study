'''
루트 1인 트리
각 노드의 부모 찾기
bfs()를 호출할 때 이전(=부모)노드를 실어 보낼까
=> dq에 넣을 떄 부모도 같이 넣기
'''
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
# padding. graph[1]부터 관리
graph = [[] for _ in range(n + 1)] # 인접리스트 사용 (<-> 인접행렬)
visited = [False] * (n + 1)
parents = [0] * (n + 1) # 정답배열. idx 2부터 출력
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(parent):
    visited[parent] = True
    dq = deque([(parent)])
    while dq:
        parent = dq.popleft()
        for child in graph[parent]:
            if not visited[child]:
                dq.append(child)
                visited[child] = True
                parents[child] = parent # 부모 저장

for node in range(1, n + 1):
    if not visited[node]:
        bfs(node) # 부모노드를 인자로

# 정답 출력
for node in parents[2:]:
    print(node)
