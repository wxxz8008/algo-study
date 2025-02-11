'''
n: 입국심사 기다리는 사람 수
times: 각 심사관이 한 명을 심사하는데 걸리는 시간

모든 사람이 심사를 받는데 걸리는 시간의 최솟값 return

`심사관마다 심사하는데 걸리는 시간은 다릅니다.` -> 이분탐색 중 문제를 한정시키기 위해 준 것 (겹치는 값이 없음)
'''
def solution(n, times):
    start, end = 1, min(times) * n # 소요시간의 총합 탐색
    while start <= end:
        cnt = 0 # 가정한 mid라는 총 시간으로 몇 명을 심사할 수 있는지 세는 변수
        mid = (start + end) // 2
        for time in times:
            cnt += mid // time
        
        if cnt >= n: # 너무 많이 심사함 => mid가 너무 큼 && cnt == n이어도 mid가 더 작은 값이 있을 수 있음
            end = mid - 1
        elif cnt < n: # 너무 적게 심사함 => mid가 너무 작음 
            start = mid + 1 
    
    return start

'''
# review
왜 start로 수렴하는지 이해가 잘 안된다,, 외워야 하나
'''
