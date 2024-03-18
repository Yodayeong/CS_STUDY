#SWEA 1206

#양쪽 모두 거리 2이상의 공간이 확보될 때 조망권이 확보된다.

#조망권이 확보된 세대의 수 반환

#해당 수 왼쪽 2개, 오른쪽 2개와 비교해서 차이값이 가장 적은 값을 출력
#이때, 값이 마이너스가 나오는 순간 바로 다음 수로 건너뜀

for _ in range(1, 11):
    n = int(input())
    heights = list(map(int, input().split()))

    answer = 0
    for i in range(2, n - 2):
        difference1 = heights[i] - heights[i - 2]
        if difference1 > 0:
            difference2 = heights[i] - heights[i - 1]
            if difference2 > 0:
                difference3 = heights[i] - heights[i + 1]
                if difference3 > 0:
                    difference4 = heights[i] - heights[i + 2]
                    if difference4 > 0:
                        answer += min(difference1, difference2, difference3, difference4)
    print(f"#{_} {answer}")