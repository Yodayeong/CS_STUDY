#SWEA 5215

#햄버거 맛은 최대한 유지하면서, 정해진 칼로리를 넘지 않는 햄버거 주문

#햄버거 재료에 대한 점수, 가게에서 제공하는 칼로리가 주어졌을 때,
#정해진 칼로리 이하의 조합 중에서, 민기가 가장 선호하는 햄버거 조합

#같은 재료 여러 번 사용 불가

#제한 칼로리 이하의 조합 중에서, 가장 맛에 대한 점수가 높은 햄버거 점수 출력

#1개~n개 모든 조합을 구한 후, 그 중 최대 출력!

#파이썬 continue
#=> 다음 코드를 실행하지 않고 건너뜀!

from itertools import combinations

T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    
    max_point = 0
    for i in range(1, N + 1):
        for value in combinations(data, i):
            calory = 0
            point = 0
            
            for v in value:
                calory += v[1]
                point += v[0]
            
            if calory > L:
                continue
            if point > max_point:
                max_point = point
                
    print(f"#{tc} {max_point}")