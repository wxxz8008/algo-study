'''
수강신청에 성공한 인원 출력하기

'''
from collections import deque, defaultdict
import sys
input = sys.stdin.readline

k, l = map(int, input().split()) # k: 수강 가능 인원 / l: 클릭 학생 수
students = deque([])
dd = defaultdict(int)

for _ in range(l):
    student = input().rstrip()
    # dd의 value가 0이 되어야 출력 가능하도록
    students.append(student)
    dd[student] += 1

cnt = 0
for student in students:
    dd[student] -= 1
    if dd[student] == 0:
        print(student)
        cnt += 1
    if cnt == k:
        break
