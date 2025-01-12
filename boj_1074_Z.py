'''
2**n X 2**n 정사각형 배열
N <= 15
0 <= r, c < 2**N
r, c 최대 대략 32 * 1_000이니까 완전탐색 불가능

ㅁㅁ --> 이렇게 네 개로 나눌 수 있음
ㅁㅁ
'''
n, r, c = map(int, input().split()) # 2**n, (r, c)
side = 2 ** n # 한 변의 길이
start, end = 1, side ** 2 # 정사각형 영역에서 시작과 끝의 숫자를 담은 변수

# 한 변의 길이를 계속 가지고 다니면서, 변의 길이가 4가 되면 멈추기
def divide(start, end):
    print(start, end)
    global side
    if side == 1:
        # 여기서 최종 계산
        print(start - 1)
        return
    mid = side // 2 # mid 두 개 중 왼쪽의 수 # (r, c)와 비교
    side //= 2
    gap = side ** 2

    print("mid", mid)
    # 1사분면
    if 0 <= r < mid and mid <= c:
        start += gap
        end = start + gap - 1
    # 2사분면
    elif 0 <= r < mid and 0 <= c < mid:
        end = start + end - 1
    # 3사분면
    elif mid <= r and 0 <= c < mid:
        start = gap * 2
        end = start + gap - 1
    # 4사분면
    elif mid <= r and mid <= c:
        start = end - gap + 1

    divide(start, end)

divide(start, end)
