#4. 땅따먹기

#각 행의 4칸 중, 한 칸만 밟으며 내려옴
#같은 열을 연속해서 밟을 수는 없음

#마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값 return

#모든 조합을 구하고, 그 중 최댓값 return하자!

#0~3
#4~12

def solution(land):
    arr = land[0]
    
    for _ in range(len(land) - 1):
        end_point = len(arr)
        
    
    

N = int(input())
land = [list(map(int, input().split(", "))) for _ in range(N)]
print(solution(land))