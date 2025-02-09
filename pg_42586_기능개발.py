def solution(progresses, speeds):
    answer = []
    
    while progresses:
        # 1씩 증가
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        over_100_cnt = 0
        pop_cnt = 0
        for i in range(len(progresses)):
            if progresses[i] >= 100: 
                over_100_cnt += 1
                pop_cnt += 1
            else:
                break
        if over_100_cnt:
            answer.append(over_100_cnt)
        for _ in range(pop_cnt):
            progresses.pop(0)
            speeds.pop(0)

    return answer
