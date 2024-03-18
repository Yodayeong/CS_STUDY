#SWEA 1954

T = int(input())
dir_row = [0, 1, 0, -1]
dir_col = [1, 0, -1, 0]

for _ in range(1, T + 1):
    n = int(input())
    snail = [[0] * n for i in range(n)]
    
    now_dir = 0
    x = y = 0
    for j in range(1, n * n + 1):
        snail[x][y] = j
        x += dir_row[now_dir]
        y += dir_col[now_dir]
        
        if x >= n or y >= n or snail[x][y] != 0:
            x -= dir_row[now_dir]
            y -= dir_col[now_dir]
            
            now_dir = (now_dir + 1) % 4
            x += dir_row[now_dir]
            y += dir_col[now_dir]
    
    print(f"#{_}")
    for a in range(n):
        for b in range(n):
            print(snail[a][b], end=" ")
        print("")
        