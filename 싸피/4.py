#SWEA 1966

T = int(input())

for _ in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    
    print(f"#{_} ", end="")
    for i in range(len(nums)):
        if i == len(nums) - 1:
            print(nums[i])
        else:
            print(nums[i], end=" ")