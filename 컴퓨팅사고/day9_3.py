#3. N개의 최소공배수

def solution(arr):    
    num_ = max(arr)
    while True:
        flag = 0
        for a in arr:
            if num_ % a != 0:
                flag = 1
        if flag == 0:
            break
        else:
            num_ += 1
    return num_

arr = list(map(int, input().split(",")))
print(solution(arr))