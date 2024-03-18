#SWEA 1859

#N일 동안의 매매가를 알고 있음
#최대 1만큼 구입 가능
#판매는 얼마든지 가능

#dp...?
#이거를 팔때랑 안팔때를 비교해서 더 큰거 저장...?

T = int(input())

for i in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    
    answer = 0
    max_num = numbers[-1]
    for j in range(len(numbers) - 1, -1, -1):
        if numbers[j] > max_num:
            max_num = numbers[j]
        else:
            difference_ = max_num - numbers[j]
            # print("difference: ", difference_, "max_num: ", max_num)
            if difference_ > 0:
                answer += difference_
            # print(answer)
    print(f"#{i} {answer}")