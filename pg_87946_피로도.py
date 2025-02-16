'''
k: 현재 피로도
["최소 필요 피로도", "소모 피로도"] 
max(던전의 개수) = 8 
=> 8! 

1) permutations 이용하기
2) 순열 함수 구현하기

'''
# 1) permutations 이용하기
# from itertools import permutations as pm
# def solution(k, dungeons):
#     answer = -1
    
#     for pairs in pm(dungeons, len(dungeons)):
#         hp = k
#         cnt = 0
#         for minHp, need in pairs:
#             if hp >= minHp:
#                 hp -= need # 피로도 감소
#                 cnt += 1
#                 continue
#             break
#         answer = max(answer, cnt)
    
#     return answer

# 2) 순열 함수 구현하기 => 백트래킹 !!

answer = 0
def solution(k, dungeons):
    global answer
    
    visited = [False] * len(dungeons)
    go(k, dungeons, 0, visited)
    
    return answer 

def go(k, dungeons, cnt, visited): # k = 현재 피로도
    global answer
    
    # 갱신
    answer = max(answer, cnt)
    
    for i in range(len(dungeons)):
        minHp, exhaust = dungeons[i][0], dungeons[i][1] # 최소필요피로도, 소모피로도
        
        if k >= minHp and not visited[i]: 
            visited[i] = True
            go(k - exhaust, dungeons, cnt + 1, visited)
            visited[i] = False



