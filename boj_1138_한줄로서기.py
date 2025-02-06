'''
- 자신의 왼쪽에 있는 큰 사람의 수를 기록함
- 키는 모두 다름
- N명의 사람

키가 큰 사람부터 (= 배열의 역순으로) 배열에 밀어넣다보면
'왼쪽에 있는 큰 사람의 수'가 결국은 N번 째 사람의 index가 된다는 것을 알 수 있음
'''

n = int(input())
li = list(map(int ,input().split()))
ans = []

for idx, num in reversed(list(enumerate(li))):
    ans.insert(num, idx + 1)

print(*ans)
