'''
bfs
queue가 비는 순간 answer += 1 해주면 됨
(연결된 것들만 queue에 연속적으로 담을 것이므로)
'''

from collections import deque

def solution(n, computers):
    answer = 0
    dq = deque()
    visited = [False] * n
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and not visited[i]:
                visited[i] = True
                dq.append(j)
                while dq:
                    node = dq.popleft()
                    visited[node] = True
                    for k in range(n):
                        if computers[node][k] == 1 and not visited[k]:
                            dq.append(k)
                answer += 1
    return answer



