'''
방문하지 않은 점에 대해서 탐색하는 것은 결국 똑같다.

다만, 방문했을 때 방문 체크를 하는 것이 아니다.
=> 맨 처음 노드는 마지막에 다시 방문할 수도 있으므로 다음 노드 기준으로 방문 체크한다.

'''
# 1. BFS
from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0 for _ in range(n)] for _ in range(n)] # 0 == False

def bfs(start): 
    line_visited = [0 for _ in range(n)]
    dq = deque()
    dq.append(start)
    while dq:
        nodeA = dq.popleft()
        for nodeB in range(n):
            if graph[nodeA][nodeB] == 1 and line_visited[nodeB] == 0:
                line_visited[nodeB] = 1
                visited[start][nodeB] = 1
                dq.append(nodeB)
for i in range(n):
    bfs(i) # start node
            
for i in range(n):
    print(*visited[i])

'''
# review
정답률에 비해 많이 헤맸던 문제
'''
