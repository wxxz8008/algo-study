'''
번호의 수: 1_000_000개
번호의 길이: 20
'''
from collections import defaultdict

def solution(phone_book):
    answer = True
    dic = defaultdict(int)
    
    # 모든 접두사가 들어간 dic 만들기
    for number in phone_book:
        for i in range(1, len(number) + 1):
            dic[number[0 : i]] += 1
    
    # 1을 초과하는 값 찾기 (자기 자신 제외)
    for number in phone_book:
        if dic[number] > 1:
            return False
    
    return answer
