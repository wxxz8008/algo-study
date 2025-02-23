'''
각각의 최소는 구할 수 있음

min(정방향, 역방향)
&& 'A'가 나타나면 flag 같은 것 표시?

-> 쭉 왼쪽으로, 쭉 오른쪽으로만 갈 수 있는 방법 말고
   왔다 갔다도 할 수 있다는 것을 간과했다..
   https://html-jc.tistory.com/650
'''
def solution(name):
    sum = 0
    # 1. 알파벳 변경
    for c in name:
        sum += min(ord(c) - 65, abs(ord(c) - 90) + 1) 
    # sum += len(name) - 1 # 커서를 최대한 움직였다고 가정
    
    # 2. 커서 위치 변경
    goCnt, backCnt = 0, 0
    # go
    for i in range(1, len(name)):
        if name[i:] == 'A' * (len(name) - i):        
            break
        goCnt += 1

    # back
    name_rev = name[0] + name[len(name)-1:0:-1]
    for i in range(1, len(name_rev)):
        if name_rev[i:] == 'A' * (len(name_rev) - i):        
            break
        backCnt += 1        
    sum += min(goCnt, backCnt)

    return sum
