#BOJ 3986

#짝을 맞춰주는 거는 "스택"을 쓰자!

import sys

n = int(input())

cnt = 0
for i in range(n):
    word_ = sys.stdin.readline().rstrip()
    word_list = []
    
    for j in range(len(word_)):
        if len(word_list) == 0:
            word_list.append(word_[j])
        
        else:
            word_list.append(word_[j])
            if word_list[-1] == word_list[-2]:
                word_list.pop()
                word_list.pop()
    
    if len(word_list) == 0:
        cnt += 1
        
print(cnt)