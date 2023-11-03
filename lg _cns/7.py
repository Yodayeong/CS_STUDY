#BOJ 4375

#부르트포스로 풀면 시간초과 문제가 발생!
#아예 1의 자리가 늘어나는 수가, 해당 n으로 나눠지는지만 판별하면 됨!

while True:
    #EOF error 해결
    try:
        n = int(input())
    except:
        break
    
    num = 0
    while True:
        num = num * 10 + 1
        if num % n == 0:
            print(len(str(num)))
            break