#SWEA 2806

#퀸은 같은 행, 열, 또는 대각선 위에 있는 말을 공격할 수 있다.

#N * N 보드에 N개의 퀸을, 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수

#백트래킹
#임의의 집합(set)에서
#주어진 기준(criterion)대로
#원소의 순서(sequence)를 선택하는 문제를 푸는 데 적합!

#n-Queens 문제
# - 임의의 집합(set): 체스보드에 있는 n*n개의 가능한 위치
# - 기준(criteria): 새로 놓을 퀸이, 다른 퀸을 위협할 수 없음
# - 원소의 순서(sequence): 퀸을 놓을 수 있는 n개의 위치

#How to Prune? How to determine Promising?
#=> Promising Function!

#깊이가 i
#=> i번째 깊이의 col이 promising 한 지 check!

# def n_queens(i, col):
#     n = len(col) - 1
#     if(promising(i, col)):
#         if(i == n): #끝까지 다 돌았다면, 정답
#             print(col[1: n + 1])
#         else: #아니면, 더 돌아야함
#             for j in range(1, n + 1):
#                 col[i + 1] = j
#                 n_queens(i + 1, col)
                
# def promising(i, col):
#     k = 1
#     flag = True
#     while(k < i and flag):
#         if(col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
#             flag = False
#         k += 1
#     return flag

def promising()
    

T = int(input())

for tc in range(T):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    print(board)
    
    for i in range(N):
        #첫째 줄에 하나씩 둔다.
        board[0][i] = 1
        
        #n-Queens
        for j in range(N - 1):
            
            for k in range(N):
                
            #promising 하면, 두기.
            
            #안하면, 다시 0으로.
        
        #다시 돌려 놓는다.
        board[0][i] = 0