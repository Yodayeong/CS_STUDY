#BOJ 2828

#1. 떨어지는 사과의 위치가 바구니보다 왼쪽이면, 왼쪽을 해당 사과의 위치랑 맞추기
#2. 떨어지는 사과의 위치가 바구니보다 오른쪽이면, 오른쪽을 해당 사과의 위치랑 맞추기

N, M = map(int, input().split())
t = int(input())

start = 1
end = M
answer = 0
for i in range(t):
    location = int(input())
    
    if location < start:
        distance = start - location
        answer += distance
        start = location
        end -= distance
    elif location > end:
        distance = location - end
        answer += distance
        end = location
        start += distance
    
print(answer)