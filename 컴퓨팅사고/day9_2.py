#2. 피보나치 수

fibonacci = [0, 1, ]

def solution(s):    
    if s > 1:
        for i in range(2, s + 1):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return fibonacci[s] % 1234567

s = int(input())
print(solution(s))