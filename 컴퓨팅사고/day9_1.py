#1. 최댓값과 최솟값

#문자열 s에는 공백으로 구분된 숫자들이 저장됨

#str에 나타나는 숫자를 "(최소값) (최대값)" 형태의 문자열을 반환하는 함수, solution 완성

def solution(s):    
    numbers = list(map(int, s.split()))
    max_ = max(numbers)
    min_ = min(numbers)
    
    return f"({min_}) ({max_})"

s = input()
print(solution(s))
