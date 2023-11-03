#BOJ 4659

#구현 문제

check_ = ['a', 'e', 'i', 'o', 'u']

while True:
    flag = 0 #flag 초기화......
    word_ = input()
    
    if word_ == "end":
        break
    
    cnt = 0
    for w in word_:
        if w in check_:
            cnt += 1
            
    if cnt == 0:
        flag = 1
    
    for i in range(len(word_) - 2):
        if word_[i] in check_ and word_[i + 1] in check_ and word_[i + 2] in check_:
            flag = 1
        elif not(word_[i] in check_) and not(word_[i + 1] in check_) and not(word_[i + 2] in check_):
            flag = 1
    
    for i in range(len(word_) - 1):
        if word_[i] == word_[i + 1]:
            if word_[i] != "e" and word_[i] != "o":
                flag = 1
       
    if flag == 1:
        print(f"<{word_}> is not acceptable.")
    else:         
        print(f"<{word_}> is acceptable.")
