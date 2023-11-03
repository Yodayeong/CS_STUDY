#BOJ 1213

#영어가 주어졌을 떄, 이를 펠린드롬으로 만들어라.
#불가능할 때는, "I'm Sorry Hansoo"를 출력
#정답이 여러개일 떄는, 사전 순으로 앞서는 것을 출력

#ABB
#AABB
#AAABB
#AB
#AAABBB
#=> 둘다 홀수면 안됨.

#AAAABBC
#=> 무조건 하나만 홀수가 가능.

##딕셔너리 정렬
#d2 = sorted(d1.items())

##한 줄의 입력을 받고, 공백 제거
#import sys
#word_ = sys.stdin.readline().rstrip()

##collections
#=> dict 형태로 현재 어떤 문자가 몇 개 있는지 저장
#import collections
#word_check = collections.Counter(word_)

import sys
import collections

cnt = 0
mid = ''
result = ''

word_ = sys.stdin.readline().rstrip()
word_check = collections.Counter(word_)
word_checked = sorted(word_check.items())

for w, v in word_checked:
    if v % 2 != 0:
        cnt += 1
        mid += w
    result += (w * (v // 2))
    if cnt > 1:
        print("I'm Sorry Hansoo")
        exit()
        
print(result + mid + result[::-1])