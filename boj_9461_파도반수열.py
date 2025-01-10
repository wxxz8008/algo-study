'''
P(n) 구하기
'''
T = int(input())
li = [0, 1, 1, 1, 2] # li[n] = li[n-1] + li[n - 5]
for i in range(5, 101):
    li.append(li[i - 1] + li[i - 5])

for _ in range(T):
    n = int(input())
    print(li[n])

'''
# review
쉽게 규칙을 찾으면 되는 문제 == dp
'''
