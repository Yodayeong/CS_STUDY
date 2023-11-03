#BOJ 2910

#등장하는 빈도가 많은게 앞으로
#빈도가 같다면, 먼저 나온게 앞으로

import collections

N, C = map(int, input().split())
message = list(map(int, input().split()))
message_ = collections.Counter(message)
message_sorted = sorted(message_.items(), key=lambda item: item[1], reverse=True)

for m, c in message_sorted:
    for i in range(c):
        print(m, end=" ")