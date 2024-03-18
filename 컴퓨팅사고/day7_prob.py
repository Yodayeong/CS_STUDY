#list()는 항목들을 저장하는 컨테이너로서, 그 안에 항목들이 순서를 가지고 저장된다.
#리스트는 어떤 타입의 항목이라도 지정할 수 있다.

#음수 인덱스는 리스트의 끝에서부터 매겨진다.
#인덱스가 적정 범위에 있는지를 신경써야 한다.

#zip()함수는 2개의 리스트를 받아서, 항목 2개를 묶어서 제공한다.
questions = ["name", "guest", "color"]
answers = ["Kim", "파이썬", "blue"]
for q, a in zip(questions, answers):
    print(f"What is your {q}? It is {a}")
    
#append()함수

#insert()함수
heroes = ["아이언맨", "토르", "헐크"]
heroes.insert(1, "스파이더맨")
print(heroes)

#index()함수
if "헐크" in heroes:
    print(heroes.index("헐크"))
    
#항목의 저장 위치를 안다면, pop() 사용
#항목의 값만 알고 있다면, remove() 사용

heroes.pop(1)
heroes.remove("헐크")
print(heroes)

#sum => 합계
#min, max => 최소값, 최대값

#sort
a = [3, 2, 1, 5, 4]
a.sort()
print(a)

a.sort(reverse=True)
print(a)

numbers = sorted(a)
print(numbers)

#리스트에서 랜덤으로 선택하기
import random

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(numberList))

#리스트 복사하기
temps = [28, 31, 33, 35, 27, 26, 25]
values = temps #얕은 복사
values = list(temps) #깊은 복사

#역순으로
print(temps[::-1])

#함수
def get_area(radius):
    area = 3.14 * radius ** 2
    return area

result = get_area(3)
print("반지름이 3인 원의 면적=", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed = numbers[::-2]
print(reversed)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[1:] = []
print(numbers)

#리스트 함축
prices = [135, -545, 922, 356, -992, 217]
mprices = [i if i > 0 else 0 for i in prices]
print(mprices)

#누적값 리스트
list1 = [10, 20, 30, 40, 50]
list2=[sum(list1[0:x+1]) for x in range(0, len(list1))]

print(list1)
print(list2)

#피타고라스 삼각형
new_list = []
for x in range(1, 30):
    for y in range(1, 30):
        for z in range(1, 30):
            if x**2 + y**2 == z**2:
                new_list.append((x, y, z))

print(new_list)

#2차원 리스트의 동적 생성
rows = 3
cols = 5

s = []
for row in range(rows):
    s += [[0] * cols]

print("s=", s)

#1차원 리스트에 합쳐지는 경우
rows = 3
cols = 5

s = []
for row in range(rows):
    s += [0] * cols

print("s=", s)

#전치 행렬
transposed = []
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("원래 행렬=", matrix)

for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print("전치 행렬=", transposed)

#1.
li_ = list(map(int, input("주어진 리스트: ").split(", ")))
li_set = set(li_)
li_sorted = sorted(li_set)
print(f"정리된 리스트: {li_sorted}")

#2.
dict_ = {}
for i in range(1, 11):
    dict_[i] = i * i

print(dict_)

#3.
d = {"Apple": 1, "Banana": 2, "Grape": 3}
for w in d:
    print(f"{w} -> {d[w]}")
    
#4.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key_ = int(input("키를 입력하시오: "))
if key_ in d:
    print(f"키 {key_}은 딕셔너리에 있습니다.")
else:
    print(f"키 {key_}은 딕셔너리에 없습니다.")
    
#5.
myDict = {"옷": 100, "컴퓨터": 2000, "모니터": 320}

sum = 0
for d in myDict:
    sum += myDict[d]
    
print(f"총합계= {sum}")

#6.
colors = ["red", "green", "blue"]
values = ["#FF0000", "#0080000", "#0000FF"]
color_dict = dict(zip(colors, values))

print(color_dict)

#7.
application_ = {}

for i in range(5):
    date = input("날짜를 입력하시오: ")
    thing = input("일정을 입력하시오: ")
    
    if date in application_:
        application_[date].append(thing)
    else:
        application_[date] = [thing]

print(application_)
        
#8.
month_print = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = int(input("달의 번호: "))
print(f"달의 번호: {month_print[month - 1]}")

#9.
sentence1 = input("첫 번째 문자열: ")
sentence2 = input("두 번째 문자열: ")

sentence_ = []
for s in sentence2:
    if s in sentence1:
        sentence_.append(s)

sentence_set = set(sentence_)
print("모두 포함된 글자: ", end="")
for s in sentence_set:
    if s != " " and s != "!":
        print(s, end=" ")
        
#10.
set1 = {10, 20, 30, 40, 50, 60}
set2 = {30, 40, 50, 60, 70, 80}

answer = set()
for s in set1:
    if s not in set2:
        answer.add(s)
for s in set2:
    if s not in set1:
        answer.add(s)
print(f"어느 한쪽에만 있는 요소들 {answer}")

# 11. 
problems = {
    "파이썬": "최근에 가장 떠오르는 프로그래밍 언어",
    "변수": "데이터를 저장하는 메모리 공간",
    "함수": "작업을 수행하는 문장들의 집합에 이름을 붙인것",
    "리스트": "서로 관련이 없는 항목들의 모임",
}

for problem in problems:
    print("다음은 어떤 단어에 대한 설명일까요?")
    print(f"\"{problems[problem]}\"")
    print("(1)파이썬 (2)변수 (3)함수 (4)리스트")
    answer = input()
    if problem == answer:
        print("정답입니다. !")
    else:
        print("오답입니다. !")

#12.
words = list(input("문자열을 입력하시오: ").split())
bad_words = list(input("금칙어를 입력하시오: ").split())

for word in words:
    if word in bad_words:
        for i in range(len(word)):
            if i == len(word) - 1:
                print("*", end=" ")
            else:
                print("*", end="")
    if word not in bad_words:
        print(word, end=" ")

#13.
word_dict = {
    "LETTERS": 0,
    "DIGITS": 0
}

word_ = input()
for w in word_:
    if w != " ":
        if w.isdigit() == False:
            word_dict["LETTERS"] += 1
        else:
            word_dict["DIGITS"] += 1

print(f"\"{word_}\" -> {word_dict}")

#14.
input_ = list(input("MM/DD/YYYY형식으로 날짜 입력: ").split("/"))

print("\"", end="")
for i in range(len(input_)):
    if i == len(input_) - 1:
        print(input_[i], end="\"")
    else:
        print(input_[i], end="/")
print(f" -> \"{input_[-1] + input_[0] + input_[1]}\"")

#15.
studentList = {
    "Park": "Korea",
    "Sam": "USA",
    "Sakura": "Japan"
}

for s in studentList:
    print(f"\"Hi! I'm {s}, and I'm from {studentList[s]}\"")

#16.
import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},;:.-_/\\?+*#"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 8

password = "".join(random.sample(all, length))
print(f"생성된 암호 = {password}")