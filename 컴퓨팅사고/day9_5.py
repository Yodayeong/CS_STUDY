#5. 가장 큰 수

#0 또는 양의 정수가 주어졌을 때,
#정수를 이어 붙여 만들 수 있는 가장 큰 수

#조합들을 고르고, 

#리스트의 모든 조합 구하기
#permutations -> 순서가 상관 있는
#combinations -> 순서가 상관 없는

from itertools import permutations

def solution(numbers):
    number_list = list(permutations(numbers, len(numbers)))
    
    max_ = 0
    for number in number_list:
        temp = ""
        for n in number:
            temp += str(n)
        if int(temp) > max_:
            max_ = int(temp)
    return max_

numbers = list(map(int, input().split(", ")))
print(solution(numbers))