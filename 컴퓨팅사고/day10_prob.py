#1. 나머지 구하기

def solution(num1, num2):
    return num1 % num2

#2. 짝수의 합

def solution(n):
    answer = 0
    
    for i in range(n + 1):
        if i % 2 == 0:
            answer += i
            
    return answer

#3. 가위 바위 보

# 가위는 2, 바위는 0, 보는 5
# 문자열 rsp가 주어질 때, 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return

def solution(rsp):
    answer = ''
    
    for r in rsp:
        if r == "2":
            answer += "0"
        elif r == "0":
            answer += "5"
        elif r == "5":
            answer += "2"
    
    return answer

#4. ad 제거하기

def solution(strArr):
    answer = []
    
    for s in strArr:
        if "ad" not in s:
            answer.append(s)
    
    return answer

#5. 가장 큰 수 찾기

def solution(array):
    answer = []
    
    max_ = max(array)
    idx_ = array.index(max_)
    
    answer.append(max_)
    answer.append(idx_)
    
    return answer

#6. 진료 순서 정하기
def solution(emergency):
    answer = []
    
    emergency_sort = sorted(emergency, reverse=True)
    
    for e in emergency:
        idx_ = emergency_sort.index(e) + 1
        answer.append(idx_)
    
    return answer