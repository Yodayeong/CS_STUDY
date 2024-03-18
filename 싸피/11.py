#BOJ 1316

N = int(input())
cnt = N

for _ in range(N):
    word_ = input()
    
    for i in range(1, len(word_)):
        if(word_[i] == word_[i - 1]):
            pass
        elif(word_[i] in word_[0:i]):
            cnt -= 1
            break
            
print(cnt)