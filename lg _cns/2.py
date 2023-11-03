#BOJ 1436

#어떤 수에 6이 적어도 3개 이상 연속으로
#666, 1666, 2666 ....

#N번쨰로 작은 종말의 수

#부르트포스
#=> 앞에서 증가하는 경우와, 뒤에서 증가하는 경우를 모두 구하면 식이 복잡해진다.
#=> 수를 증가해나가며 666을 포함하는지 판변한다!

cnt = 1
answer = 666

n = int(input())

while True:
    if n == cnt:
        print(answer)
        exit()
    answer += 1
    if '666' in str(answer):
        cnt += 1