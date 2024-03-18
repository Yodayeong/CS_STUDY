#SWEA 1209

for tc in range(1, 11):
    n = int(input())
    numbers = [list(map(int, input().split())) for _ in range(100)]
    max_ = 0
    
    for i in range(100):
        temp = sum(numbers[i])
        if temp > max_:
            max_ = temp
            
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += numbers[j][i]
        if temp > max_:
            max_ = temp
    
    temp = 0
    for i in range(100):
        temp += numbers[i][i]
    if temp > max_:
        max_ = temp
    
    temp = 0
    cnt = 99
    for i in range(100):
        temp += numbers[i][cnt]
        cnt -= 1
    if temp > max_:
        max_ = temp

    print(f"#{tc} {max_}")