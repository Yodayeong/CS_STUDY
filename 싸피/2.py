#SWEA 1984

#Runtime Error

t = int(input())

for i in range(1, t + 1):
    numbers_ = list(map(int, input().split()))
    numbers_.sort()
    numbers_.pop(0)
    numbers_.pop()
    print(f"#{i} {round(sum(numbers_)/len(numbers_))}")
