'''
과제는 받자마자 시작하기 때문에 바로 -1 가능
stack에서 pop하면서 풀면 되는 문제
'''
import sys
input = sys.stdin.readline

stack = []
ans = 0
n = int(input())
for _ in range(n):
    inputs = list(map(int, input().split()))
    # 과제가 주어지면 stack에 쌓인 것들은 신경 쓸 필요 없음
    if len(inputs) == 3:
        if inputs[2] == 1:
            ans += inputs[1]
        else:
            stack.append((inputs[1], inputs[2] - 1))
        continue
    # 입력이 0일 때 처리
    if stack:
        score, time = stack.pop()
        if time == 1:
            ans += score
        else:
            stack.append((score, time - 1))

print(ans)
