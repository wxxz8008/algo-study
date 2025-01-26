'''
폭발 문자열
모든 폭발 후에 남는 문자열 출력하기

최초 문자열의 길이 최대 1_000_000
계속 반복문을 돌며 탐색하면 분명 시간초과
그렇다면 ?

stack은 리스트로 구현
1_000_000번 최대 길이 36을 검사한다면?
O(1_000_000 * 36) => 통과 가능

폭발의 사이클을 여러 번으로 가져가지 말고,
한 번에 다 폭발시키는 방향으로 풀이
'''
import sys
input = sys.stdin.readline

full = input().rstrip()
target = input().rstrip()
stack = []
length = len(target)

for s in full:
    stack.append(s)
    if len(stack) >= length: # 슬라이싱 가능
        if stack[-1 * length : ] == list(target):
            for k in range(length):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')

'''
# review
stack은 list로 구현되기 때문에 동일한 시간복잡도 가짐
stack[n : n + 10] => O(10)
stack[1] => O(1)
등 삽입/삭제에 불리하고 탐색엔 유리
'''
