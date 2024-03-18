#BOJ 1417
#다솜이는 기호 1번

n = int(input())
number1 = int(input())
others = []
cnt = 0

if n > 1:
    for _ in range(n - 1):
        temp = int(input())
        others.append(temp)
    
    while True:
        max_ = max(others)
        
        if number1 > max_:
            break
        else:
            cnt += 1
            max_index = others.index(max_)
            others[max_index] -= 1
            number1 += 1
print(cnt)           