#SWEA 1215

for tc in range(1, 11):
    n = int(input())
    code = [input() for _ in range(8)]
    div_ = n // 2
    answer = 0
    
    if n % 2 == 0:
        for i in range(8):
            for j in range(8 - n + 1):
                left_ = code[i][j:j + div_]
                right_ = code[i][j + div_:j + n]
                right_ = right_[::-1]
                # print(f"left_: {left_}, right_: {right_}")
                if left_ == right_:
                    answer += 1
        
        for i in range(8):
            for j in range(8 - n + 1):
                left_ = ""
                right_ = ""
                # print(f"i: {i}, j: {j}")
                for k in range(div_):
                    left_ += code[j + k][i]
                for k in range(div_, n):
                    right_ += code[j + k][i]
                right_ = right_[::-1]
                # print(f"left_: {left_}, right_: {right_}")
                if left_ == right_:
                    answer += 1
        print(f"#{tc} {answer}")
    else:
        for i in range(8):
            for j in range(8 - n + 1):
                left_ = code[i][j:j + div_]
                right_ = code[i][j + div_ + 1:j + n]
                right_ = right_[::-1]
                # print(f"left_: {left_}, right_: {right_}")
                if left_ == right_:
                    answer += 1
        
        for i in range(8):
            for j in range(8 - n + 1):
                left_ = ""
                right_ = ""
                # print(f"i: {i}, j: {j}")
                for k in range(div_):
                    left_ += code[j + k][i]
                for k in range(div_ + 1, n):
                    right_ += code[j + k][i]
                right_ = right_[::-1]
                # print(f"left_: {left_}, right_: {right_}")
                if left_ == right_:
                    answer += 1
        print(f"#{tc} {answer}")