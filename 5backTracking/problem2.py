
# 완전탐색적 사고

# 재료를 1부터 N까지 다 써보면 되겠네!

def recur(idx, A, B, C, D, E):
    global answer
    
    if idx == N:
       if a <= A and b <= B and c <= C and d <= D:
           answer = min(answer, E)

    #재료를 사용한 경우에는 영양소가 더해진다.
    recur(idx+1, A+ingre[idx][0], B+ingre[idx][1], C+ingre[idx][2], D+ingre[idx][3], D+ingre[idx][4], E+ingre[idx][5])
    #재료를 사용하지 않은 경우에는 그냥 다음 재료로 넘어간다  
    recur(idx+1, A, B, C, D, E)

N = int(input())

a,b,c,d = map(int, input().split())

ingre = [list(map(int, input().split())) for _ in range(N)]

answer = 9999999999999999

recur(0,0,0,0,0,0)

print(answer)