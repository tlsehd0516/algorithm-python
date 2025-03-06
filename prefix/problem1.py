#        1   2   3   4   5   6   7   8   9   10
# prefix 1   3   6   10  15  21  28  36  45  55

#           3   -2   -4   -9   0   3   7   13   8   -3
# 간격더하기      1   -6   -13  -9  3   10  20   21   5
# prefix    3    1    -3   -12  -12 -9  -2  11   19  16
# = 컴퓨터에게 기억하는 법을 가르쳤다!

A,B = map(int,input().split())
arr = list(map(int,input().split()))

prefix = [ 0 for _ in range(A+1)] # 1칸 더 크게 만들기!

for i in range(A):
    prefix[i+1] = prefix[i] + arr[i]


answer = []
for k in range(B, A+1):
    answer.append(prefix[k] - prefix[k-B])

print(max(answer))