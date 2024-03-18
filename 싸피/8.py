#SWEA 1244

#정해진 횟수만큼 숫자판 두 개의 위치를 교환할 수 있다.

#숫자판의 위치에 부여된 가중치에 의해 상금 계산
#오른쪽 끝에서부터 1원이고, 왼쪽으로 한자리씩 갈수록 10의 배수만큼 커짐

#반드시 횟수만큼 교환. 동일한 위치의 교환이 중복되어도 된다.

#그냥 완전탐색으로 모든 경우를 다 고려하자 !

T = int(input())

for tc in range(1, T + 1):
    number_, n = input().split()
    
    results = set([number_])
    for _ in range(int(n)):
        temp = set()
        while results:
            now_num = list(results.pop())
            for i in range(len(now_num) - 1):
                for j in range(i + 1, len(now_num)):
                    now_num[i], now_num[j] = now_num[j], now_num[i]
                    temp.add(''.join(now_num))
                    now_num[i], now_num[j] = now_num[j], now_num[i]
        results = temp
        
    max = 0
    for result in results:
        if int(result) > max:
            max = int(result)
    
    print(f"#{tc} {max}")       