#SWEA 1225

#8개의 숫자를 입력
#첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보냄
#다음 첫 번째 숫자는 2 감소한 뒤, 맨 뒤로 보냄
#5까지 감소하고, 이를 한 사이클이라 함.
#이 때, 0보다 작거나 같은 경우는 0으로 유지

for tc in range(1, 11):
    n = int(input())
    numbers = list(map(int, input().split()))
    
    cnt = 1
    while True:
        temp = numbers.pop(0)
        temp -= cnt
        if temp <= 0:
            numbers.append(0)
            break
        else:
            numbers.append(temp)
            
        if cnt == 5:
            cnt = 1
        else:
            cnt += 1
    
    print(f"#{tc} ", end="")
    for i in range(8):
        if i == 7:
            print(numbers[i])
        else:
            print(numbers[i], end=" ")   