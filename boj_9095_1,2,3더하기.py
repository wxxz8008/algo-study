'''
n (n < 11)

문제 분류 예상
1) dp
2) 재귀

while문으로 계속 판단하면 될 것 같음
'''
def diminish(n):
    global cnt
    if n == 0:
        cnt += 1
        return
    for i in range(3, 0, -1):
        if n - i >= 0:
            diminish(n - i)

T = int(input())
for _ in range(T):
    cnt = 0
    n = int(input())
    diminish(n)
    print(cnt)

''' 
# review
직접 써가며 규칙을 찾다가 (dp 접근)
그 후에 재귀로 풀 수 있음을 깨닫고 접근 변경 (재귀 접근)

처음엔 for문을 정방향으로 탐색했는데, 이후 역방향으로 변경 
'''
