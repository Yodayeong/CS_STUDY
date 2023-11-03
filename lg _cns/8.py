#BOJ 2870

#문자가 알파벳인지 숫자인지 판별
#=> isalpha() 내장함수
#=> 숫자 및 공백이 포함되어 있으면, False 반환

#0이 아닌 숫자에 대해서,
#해당 숫자 뒤의 문자도 숫자라면, 계속해서 추가해나감

n = int(input())

answer = []
number_tmp = ''
for i in range(n):
    word_ = input()
    for j in range(len(word_)):
        if word_[j].isalpha() == False:
            if number_tmp == '0':
                number_tmp = ''
            number_tmp += str(word_[j])
        else:
            if len(number_tmp) >= 1:
                answer.append(int(number_tmp))
                number_tmp = ''
    if len(number_tmp) >= 1:
                answer.append(int(number_tmp))
                number_tmp = ''
        

answer.sort()
for a in answer:
    print(a)