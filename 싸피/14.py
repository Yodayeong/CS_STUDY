#SWEA 1805

#농장의 크기는 항상 홀수
#수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = [list(map(int, input())) for _ in range(N)]
    max_ = N // 2
    answer = 0
    
    cnt = 0
    for i in range(max_, -1, -1):
        for j in range(cnt, N - cnt):
            answer += numbers[i][j]
        cnt += 1
    
    cnt = 1
    for i in range(max_ + 1, N):
        for j in range(cnt, N - cnt):
            answer += numbers[i][j]
        cnt += 1
    
    print(f"#{tc} {answer}")