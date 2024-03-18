#SWEA 1213

for tc in range(1, 11):
    n = int(input())
    find_ = input()
    string_ = input()
    len_find = len(find_)
    cnt = 0
    
    for i in range(len(string_) - len_find + 1):
        if(string_[i:i+len_find] == find_):
            cnt += 1
    
    print(f"#{tc} {cnt}")