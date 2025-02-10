'''
ex.
80까지만 담을 수 있는 배낭에
가치가 가장 높은 것들을 담기
-> 0-1 배낭문제
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n: 최대 공부시간 / k: 과목 수
scores = [0]
times = [0]
dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)] # dp[마지막 행][마지막 열]이 정답

for _ in range(k):
    score, time = map(int, input().split()) # score: 중요도 / time: 공부시간
    scores.append(score)
    times.append(time)

for i in range(1, k + 1): # 과목
    for j in range(1, n + 1): # 공부 시간
        # cf. dp[i][j] => i번 째까지의 과목을 j시간을 공부해서 얻는 최대 점수(중요도)
        if times[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j]
                           , dp[i - 1][j - times[i]] + scores[i])

print(dp[k][n])

'''
# review
물건을 쪼갤 수 없는 배낭문제 (0-1 배낭문제) => DP로 풀이

가능한 시간(=배낭 무게)의 범위 내의 수를 모두 2차원 배열의 `열`로 만들고,
과목의 수(=물건의 수)를 2차원 배열의 `행`으로 만드는 것이 포인트
'''
