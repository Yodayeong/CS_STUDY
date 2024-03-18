#SWEA 1217

for tc in range(1, 11):
    n = int(input())
    N, M = map(int, input().split())
    
    answer = 1
    for i in range(M):
        answer *= N
        
    print(f"#{tc} {answer}")