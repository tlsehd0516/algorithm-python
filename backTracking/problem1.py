# 15649

def recur(number):

    if number == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if i in arr:
            continue
        arr.append(i)
        recur(number+1)
        arr.pop()
    
    


N,M = map(int, input().split())
arr = []

recur(0)