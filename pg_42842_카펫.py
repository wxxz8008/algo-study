'''
yellow의 가능한 사각형 조합(가로 * 세로)을 찾아내고, (cf. sqrt 넘으면 pass해도 됨 - 여기서 시간 복잡도 줄이기)
그러면 해당 조합에 필요한 brown 개수까지 찾을 수 있다! 
'''

def solution(brown, yellow):
    
    for x in range(1, int(yellow ** 0.5) + 1):
        if yellow % x == 0: # x, y 모두 자연수라면
            y = yellow // x
        if (x + y) * 2 + 4 == brown:
            return [y + 2, x + 2]
