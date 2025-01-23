'''
nCm 조합 구하기
# itertools 라이브러리 사용하지 않고 풀어보기
'''
n, m = map(int, input().split())
li = [i for i in range(1, n + 1)]

def combination(part, start):
    global n, m
    # if문 - 출력 후 return
    if len(part) == m:
        print(*part)
        return
    # for문으로 값 모으기
    for i in range(start, n + 1):
        combination(part + [i], i + 1)

combination([], 1)
