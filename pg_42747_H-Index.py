from collections import defaultdict

def solution(citations):
    answer = 0
    
    dd = defaultdict(int)
    citations = sorted(citations)
    
    for citation in citations:
        dd[citation] += 1
    
    total = len(citations)
    
    # 처음 푼 방식
    '''
    for key in dd:
        if total >= key: # 3보다 큰 게 3개 이상이라면
            answer = key
        total -= dd[key]
    '''
    
    # 변경한 방식
    for i in range(max(dd) + 1):
        if total >= i:
            answer = i
        if dd[i] != 0:
            total -= dd[i]
        
    return answer
