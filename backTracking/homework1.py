# 15650

N,M = map(int, input().split())

def recur(number):

    if(len(arr) == M):
        print(*arr)
        return 
    
    for i in range(number, N+1):
        if i not in arr:
            arr.append(i)
            recur(i+1)
            arr.pop()


arr = []
recur(1)

# 4 2

# recur(1)
# arr.append(1)
# recur(2)
# arr.append(2)
# recur(3)
# print arr + arr.pop()