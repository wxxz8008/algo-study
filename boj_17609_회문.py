'''
회문(0)
유사회문(1) - 한 문자를 삭제하여 회문이 되는 문자열
일반문자열(2)

셋 중 무엇인지 판단하는 문제

문자열 길이 짝/홀에 따라 분기 처리 해야할지도

양 끝에서 투 포인터 (left, right)를 출발시킨다고 해도,
다른 점이 나왔을 때 어떤 포인터를 이동시킬지 (=누가 양보할지) 어떻게 정하지?
=> 다음 점까지 비교하여 가능성이 높은 점(=다음 점이 같은 것)에게 양보 -> 그리디스럽다고 할 수 있는건가
==> 처음 생각한 방법. 실패.
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = input().rstrip()
    length = len(s)
    left, right = 0, length - 1

    ans = 0 # 기본은 회문 (길이가 1일 때를 대비)
    while left < right:
        # 문자가 같을 때
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue
        # A. 문자가 다를 때
        # A-1. left 하나 빼기
        if s[left + 1 : right + 1] == s[left + 1 : right + 1][::-1]:
            ans = 1
            break
        # A-2. right 하나 빼기
        if s[left : right] == s[left : right][::-1]:
            ans = 1
            break
        # 어차피 일반문자열이면 탐색 멈추고 break;
        ans = 2
        break
    print(ans)

'''
# review
1. 예외처리가 지저분해지면 틀린 게 아닐까 의심해보자
2. 슬라이싱을 계속 하는 것이 아니고, 한 번만 하면 정답이 결정되므로 시간복잡도 측면에서 문제 없음
   슬라이싱 시간복잡도 최대 O(100_000) (=문자열 길이) => 한 번하고 마니까 사용해도 괜찮음! 
'''
