# 14501

# 모든 날에 상담을 받거나, 안받거나 모든 경우의 수를 확인해준다.

def recur(idx):
    global answer
    if idx == N-1:
        return 0
    if idx > N-1 :
        return -99999999999
    if dp[idx] != -1 : #이미 저장되었다면
        return dp[idx]
    # if idx > N :
    #     if idx > N+1: return
    #     answer = max(answer, price)
    #     return

    # 상담을 하거나 안하거나, 그 중에서 더 많은 돈을 버는 경우를 내 DP 테이블에 저장하겠다 
    dp[idx] = max(recur(idx + interview[idx][0]) + interview[idx][1], recur(idx+1))
   
    return dp[idx]
    

N = int(input())
interview = [list(map(int, input().split())) for _ in range(N)]

dp = [-1 for _ in range(N+1)] 

result = recur(0)
print(result)