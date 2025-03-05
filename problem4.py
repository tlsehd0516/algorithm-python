
# A가 정답으로 생각할 수 있는 모든 수를 넣어보기!

# 그리고 B가 도전한 내용이 맞는지 확인하기

n = int(input())

hint = [list(map(str, input().split())) for _ in range(n)]

# [[123,1,1], [356,1,0], ...]
answer = 0
for a in range(1,10): # 100의 자리
    for b in range(1,10): # 10의 자리
        for c in range(1,10): # 1의 자리

            if(a==b or b==c or c==a):
                continue

            # 숫자가 정해졌다면
            cnt = 0
            for arr in hint:
                number = list(arr[0])
                strike = int(arr[1])
                ball = int(arr[2])

            
                # a,b,c 라는 숫자를
                # number 하고 비교해서

                ball_count = 0
                strike_count = 0

                if int(number[0]) == a :
                    strike_count += 1
                if int(number[1]) == b :
                    strike_count += 1
                if int(number[2]) == c :
                    strike_count += 1

                if (a == int(number[1]) or a == int(number[2])) :
                    ball_count += 1
                if (b == int(number[0]) or b == int(number[2])) :
                    ball_count += 1
                if (c == int(number[0]) or c == int(number[1])) :
                    ball_count += 1

                if ball == ball_count and strike == strike_count:
                    cnt += 1

            if cnt == n:
                answer += 1

print(answer)