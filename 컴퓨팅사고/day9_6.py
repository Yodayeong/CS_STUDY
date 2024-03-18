#6. 소수 찾기

#1은 소수가 아님.

from itertools import permutations

def find_prime(n):
    flag = 0
    if n <= 1:
        flag = 1
    if n >= 3:
        for i in range(2, n):
            if n % i == 0:
                flag = 1
                break
    return flag

def solution(numbers):
    number_list = list(permutations(numbers))
    for number in numbers:
        number_list.append(number)
        
    for number in number_list:
        # temp = ""
        # if len(number) >= 2:
        for n in number:
            temp += str(n)
        # else:
        #     temp += str(number)
        print(temp)
            
        
    
        
        # for number in number_list:
        #     print(number)
            # for n in number:
            #     print(n)
            #     temp = ""
            #     for t in n:
            #         temp += str(t)
            #     print(temp)
            #     if find_prime(int(temp)) == 0:
            #         answer.append(int(temp))
    # return number_list
                    

numbers = list(map(int, input()))
print(solution(numbers))

# from itertools import permutations

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def solution(numbers):
#     answer = 0
#     # 가능한 모든 순열 생성
#     num_list = list(numbers)
#     permutations_set = set(int(''.join(p)) for p in permutations(num_list))
#     print(permutations_set)
    
#     # # 소수인지 확인하고 개수 세기
#     # for num in permutations_set:
#     #     if is_prime(num):
#     #         answer += 1

#     # return answer

# # 예제 테스트
# print(solution("17"))  # 예상 결과: 3
# print(solution("011"))  # 예상 결과: 2