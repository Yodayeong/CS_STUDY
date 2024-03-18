#SWEA 1216

#거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문이라 한다.

#가로, 세로를 모두 보아, 가장 긴 회문의 길이를 구하는 문제

for tc in range(1, 11):
    n = int(input())
    board = [input() for _ in range(100)]
    max_len = 0
    
    #1. 가로 체크
    for i in range(100):
        now = board[i]
        for j in range(100):
            start = j
            end = 100
        
            while True:
                if start >= end:
                    break
                
                # print(now[start:end])
                len_div = len(now[start:end]) // 2
                #짝수인 경우,
                if(len(now[start:end]) % 2 == 0):
                    temp = now[start + len_div: start + len(now[start:end])]
                    if now[start:start + len_div] == temp[::-1]:
                        # print(now[start:start + len_div] == temp[::-1])
                        if(len(now[start:end]) > max_len):
                            max_len = len(now[start:end])
                # print(board[i:i + len_div], board[i + len_div: i + len(board[i:end])])
            
                #홀수인 경우,
                else:
                    temp = now[start + len_div + 1: start + len(now[start:end])]
                    # print(now[start:start + len_div], temp)
                    if now[start:start + len_div] == temp[::-1]:
                        # print(now[start:start + len_div] == temp[::-1])
                        if(len(now[start:end]) > max_len):
                            max_len = len(now[start:end])
                
                end -= 1
    #2. 세로 체크
    for i in range(100):
        for j in range(100):
            start = j
            end = 100
            
            while True:
                if start >= end:
                    break
            
                temp = ""
                for k in range(start, end):
                    temp += board[k][i]
                
                # print(temp)
                if(len(temp) % 2 == 0):
                    left_ = temp[0: len(temp) // 2]
                    right_ = temp[len(temp) // 2: len(temp)]
                    # print(f"left_: {left_}, right_: {right_}")
                    if left_ == right_[::-1]:
                        # print(left_ == right_)
                        if(len(temp) > max_len):
                            max_len = len(temp)
                else:
                    left_ = temp[0: len(temp) // 2]
                    right_ = temp[len(temp) // 2 + 1: len(temp)]
                    # print(f"left_: {left_}, right_: {right_}")
                    if left_ == right_[::-1]:
                        # print(left_ == right_)
                        if(len(temp) > max_len):
                            max_len = len(temp)
                
                end -= 1
                
    print(f"#{tc} {max_len}")
