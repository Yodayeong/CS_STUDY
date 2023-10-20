list

```python
#선형구조 => 하나의 묶음으로 데이터 저장

list_ = []
list_.append(1)
list_.append(2)
list_.append(3)
print(list_) #[1, 2, 3]

list_ = []
list_.append(1)
list_.append(2)
list_.append(3)
print(list_[2]) #3

list_ = []
list_.append(1)
list_.append(2)
list_.append(3)
print(list_[0]) #1

list_ = []
list_.append(1)
list_.append(2)
list_.append(3)
print(list_[0:1]) #[1]

list_ = []
list_.append(1)
list_.append(2)
list_.append(3)
print(list_[0:2]) #[1, 2]

list_ = []
list_.append(1)
list_.append(2)
list_.append(3)
print(list_[2:]) #[3]

for i in list_:
    print(i, end=" ") #1 2 3

slist = ["영어", "수학", "사회", "과학"]
print(slist) #['영어', '수학', '사회', '과학']

print(range(5)) #range(0, 5)
print(list(range(5))) #[0, 1, 2, 3, 4]
print(list(range(1, 6))) #[1, 2, 3, 4, 5]
```

<br>

짝수인지 홀수인지 판별

- if a % 2 == 0 : 짝수
- else : 홀수

<br>

반복의 종류

- 횟수 반복(for문): 정해진 횟수만큼 반복
- 조건 반복(while문): 특정한 조건이 성립되는 동안 반복

<br>

중간점검

```python
myList = [1, 2, 3, 4, 5]
print(myList)

myList[0] = 0
print(myList)

myList[-1] = 9
print(myList)

print(len(myList))

for _ in myList:
  print("방문을 환영합니다.")
  
for i in [9, 8, 7, 6, 5]:
    print("i=", i)
```

<br>

range

```python
#간격 지정
for i in range(1, 6, 1):
    print(i, end=" ")
#1 2 3 4 5

#역순
for i in range(10, 0, -1):
    print(i, end=" ")
#10 9 8 7 6 5 4 3 2 1
```

<br>

예제

```python
#1부터 10까지의 합

#for문
sum = 0
n = 10
for i in range(1, n + 1):
    sum = sum + i
print("합=", sum)

#while문
i = 1
sum = 0

while i <= 10:
    sum += i
    i += 1

print("합계는", sum)

#구구단 출력
for i in range(1, 6):
    print("9 *", i, "=", 9 * i)
    
#1부터 10까지 중 짝수만 더하기

#첫번째 풀이
sum = 0
n = 10
for i in range(1, n + 1):
    if(i % 2 == 0):
        sum += i
print(sum)

#두번째 풀이
sum = 0
n = 10
for i in range(0, n + 1, 2):
    sum += i
print(sum)
```

<br>

중간점검

```python
#1.
for i in range(1, 5, 1):
    print(2 * i)
    
#2
#4
#6
#8

#2.   
for i in range(10, 0, -2):
    print("Student" + str(i))
    
#Student10
#Student8
#Student6
#Student4
#Student2

#3. for문을 이용하여서 팩토리얼을 계산해보자.
x = int(input("정수를 입력하시오: "))
fact = 1

for i in range(1, x + 1):
    fact *= i

print(x, "!은", fact, "이다.")

#10 !은 3628800 이다.

#4. 팩토리얼을 거꾸로 계산해보자.
x = int(input("정수를 입력하시오: "))
fact = 1

for i in range(x, 0, -1):
    fact *= i

print(x, "!은", fact, "이다.")

#10 !은 3628800 이다.
```

<br>

터틀 그래픽에서 사용자로부터 정수 n을 받아서 n-각형을 그리는 프로그램을 작성해보자.

<br>

이차방정식

```python
COUNT = 100
START = 1.0
END = 2.0

for i in range(COUNT):
    x = START + i*((END-START)/COUNT)
    f = (x**2 -x -1)
    if abs(f-0.0) <0.01:
        print("방정식의 해는 ", x)
```

<br>

이자율

```python
TARGET = 2000 #목표금액
money = 1000 #초기자금
year = 0 #연도
rate = 0.07 #이자율

#현재 금액이 목표 금액보다 적으면 반복한다.
while money < TARGET:
    money = money + money * rate
    year += 1

print(year, "년")
```

<br>

숫자 맞추기 게임

```python
import random

tries = 0
guess = 0
answer = random.randint(1, 100)

print("1부터 100 사이의 숫자를 맞추시오")

while guess != answer:
    guess = int(input("숫자를 입력하시오: "))
    tries += 1
    
    if guess < answer:
        print("너무 낮음!")
    elif guess > answer:
        print("너무 높음!")

if guess == answer:
    print("축하합니다. 시도횟수=", tries)
    print("정답은", answer)
```

<br>

별 찍기

```python
for y in range(5):
    for x in range(10):
        print("*", end="")
    print("")

#**********
#**********
#**********
#**********
#**********

for y in range(1, 6):
    for x in range(y):
        print("*", end="")
    print("")
    
#*
#**
#***
#****
#*****

for y in range(5, 0, -1):
    for x in range(y):
        print("*", end="")
    print("")

#*****
#****
#***
#**
#*
```

<br>

소수 찾기 - 1과 자기 자신으로만 나뉘어짐 => 어떤 형태로든 시험 냄!!!!!