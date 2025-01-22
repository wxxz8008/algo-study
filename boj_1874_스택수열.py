'''
임의의 수열 -> stack으로 만들기

stack에 반드시 '오름차순'으로 push 해야 함
임의의 수열이 주어질 때, stack으로 이 수열을 만들 수 있는지 없는지 판단
'''
import sys
input = sys.stdin.readline

n = int(input())
target, stack = [], []
ans = []
for _ in range(n):
    target.append(int(input()))
target = target[::-1] # 순수 stack을 사용하기 위해 역순 처리
# target <- num
for num in range(1, n + 1):
    # 1. num에 넣기
    stack.append(num)
    ans.append("+")

    while stack: # 배열이 빈 경우 처리
        # 2-1. 동일한 숫자라면 빼기
        if target[-1] == stack[-1]:
            target.pop()
            stack.pop()
            ans.append("-")
            continue
        # 2-2. 동일하지 않다면
        break
if target:
    print("NO")
else:
    for i in ans:
        print(i)
