# strike ball 카운트를 계산할때
# 어렵게 생각하지 않고

# A라는 친구가 생각할 수 있는 정답의 범위를 모조리때려박아서
# 조건에 모두 맞다면! 정답 카운트를 올리겠다

# 100 ~ 999

import sys
sys.setrecursionlimit(9999999) # 파이썬은 재귀함수 1000번이면 끝이난다(디폴트)

def checker(idx, number):
    _number = hint[idx][0]
    _strike = hint[idx][1]
    _ball = hint[idx][2]



    strike = 0
    ball = 0

    _A = _number // 100
    _B = (_number - (_A*100)) // 10
    _C = _number % 10 

    A = number // 100
    B = (number - (A*100)) // 10
    C = number % 10 

    if(A == 0 or B == 0 or C == 0):
        return False
    if(A==B or A==C or B==C):
        return False
    
    if(A==_A):
        strike +=1
    if(B==_B):
         strike +=1
    if(C==_C):
         strike +=1
    if(A==_B or A==_C):
        ball +=1
    if(B==_A or B==_C):
        ball +=1
    if(C==_A or C==_B):
        ball +=1

    if(strike == _strike and ball == _ball):
        return True
    
    return False

answer = 0

def recur(hint_idx, number):
    global answer
    if hint_idx == 4:
        answer += 1
        recur(0, number+1)
        return
    
    if number == 1000:
        return
    # 만약에 힌트에 통과했다면
    if checker(hint_idx, number):
        recur(hint_idx+1, number)
    else:
        recur(0, number+1)


n = int(input())

hint = [list(map(int, input().split())) for _ in range(n)]



recur(0,100)
print(answer)