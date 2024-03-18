#SWEA 1208

#높은 곳의 상자를 낮은 곳으로 옮겨, 최고점과 최저점의 간격을 줄임

#작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옯기는 작업 후, 최고점과 최저점의 차이 반환

for tc in range(1, 11):
    n = int(input())
    heights = list(map(int, input().split()))
    length_ = len(heights)
    
    for _ in range(n):
        max_ = max(heights)
        min_ = min(heights)
        max_index = heights.index(max_)
        min_index = heights.index(min_)
        # print("max_index: ", max_index, "min_index: ", min_index)
        
        heights[max_index] -= 1
        heights[min_index] += 1
        
    max_ = max(heights)
    min_ = min(heights)
    print(f"#{tc} {max_ - min_}")