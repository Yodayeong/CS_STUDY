#SWEA 1289

#특정 bit을 0인지 1인지 결정하면, 해당 값이 메모리 끝까지 덮어씌움

#원래 상태가 주어질 때,
#초기화 상태(모든 bit이 0)에서 원래 상태로 돌아가려면,
#최소 몇 번 고쳐야 하는지.

#젤 처음 1을 check하고, 그 후로 몇 번 변하는 지 check!

T = int(input())

for tc in range(1, T + 1):
    now = 0
    cnt = 0
    numbers = list(map(int, input()))
    for number in numbers:
        if number != now:
            now = number
            cnt += 1
    print(f"#{tc} {cnt}")