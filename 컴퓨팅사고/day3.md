```python
#problem1

x = int(input("x: "))
y = int(input("y: "))

print("두수의 합: " + str(x + y))
print("두수의 차: " + str(x - y))
print("두수의 곱: " + str(x * y))
print("두수의 평균: " + str((x + y)/2))
print("큰수: " + str(max(x, y)))
print("작은수: " + str(min(x, y)) + "\n")

#problem2

chicken = int(input("닭의 수: "))
pork = int(input("돼지의 수: "))
cow = int(input("소의 수: "))

print("\n전체 다리의 수: " + str(2 * chicken + 4 * pork + 4 * cow) + "\n")

#problem3

x = int(input("삼각형의 첫 번째 변의 길이: "))
y = int(input("삼각형의 두 번째 변의 길이: "))
print("삼각형의 나머지 변의 최대 길이 = " + str(x + y - 1) + "\n")

#problem4

hour = int(input("시간을 입력하시오: "))
minute = int(input("분을 입력하시오: "))
print(str(hour) + " 시간 " + str(minute) + " 분은 " + str(60 ** 2 * hour + 60 * minute) + " 초입니다.\n")

#problem5
ferenheit = int(input("화씨 온도를 입력하시오: "))
celsius = (ferenheit - 32) * 5 / 9

print("화씨 " + str(ferenheit) + "도는 섭씨 " + "{:.2f}".format(celsius) + "도에 해당합니다.\n")
```





시험 문제 냈었음

```python
a = 2*2//2
b = 3//2*3
print(a, b)
```

<br>

문자열

```python
#문자열은 사전식으로 정렬됨
s1 = "Audrey Hepburn"
s2 = "Grace Kurly"

print(s1 < s2) #True
```

<br>

실수비교

```python
print(0.1 + 0.1 + 0.1)
#0.30000000000000004 =>0.3과 비교하면 false 반환함
```

<br>

산수문제 출력

```python
import random

x = random.randint(1, 100)
y = random.randint(1, 100)

answer = int(input(f"{x} + {y} = "))ㅅ

flag = (answer == (x + y))
print(flag)
```

<br>

조건문

```python
#산술 퀴즈 프로그램
x = int(input("정수를 입력하시오: "))

if x%2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
    
#조건 연산자 예제
x = int(input("첫 번째 수 ="))
y = int(input("두 번째 수 ="))
max_value = (x if x > y else y)
min_value = (x if x < y else y)
print("큰 수=", max_value, "작은 수=", min_value)

#양수인지 음수인지 판별

x = int(input("값을 입력해주세요."))

if(x >= 0):
    print("양수입니다.")
else:
    print("음수입니다.")

#사용자의 성적이 60 이상이면 합격
grade = int(input("성적을 입력해주세요."))

if(grade >= 60):
    print("합격입니다.")
else:
    print("불합격입니다.")
    
#백화점 안내 메시지    
price = int(input("정가를 입력하시오: "))

if(price >= 100):
    print("10층에서 사은품을 받아가세요.")
    print("할인된 가격= " + str(price * 0.85))
else:
    print("할인된 가격= " + str(price * 0.9))
    
#물의 상태
temp = float(input("온도를 입력사히오: "))

if(temp <= 0):
    print("물의 상태는 얼음입니다.")
elif (temp > 0 and temp < 100):
    print("물의 상태는 액체입니다.")
else:
    print("물의 상태는 기체입니다.")

#동전 던지기 게임
print("동전 던지기 게임을 시작합니다.")

coin = random.randrange(2)

if(coin == 0):
    print("앞면입니다.")
else:
    print("뒷면입니다.")

print("게임이 종료되었습니다.")
```

<br>

터틀 그래픽스

```python
import turtle

t = turtle.Turtle()

t.shape("turtle")

t.width(3)

#거북이를 3배 확대한다.
t.shapesize(3, 3)

while True:
  command = input("명령을 입력하시오:")
  if command == "i":
    t.left(90)
    t.forward(100)
  if command == "r":
    t.right(90)
    t.forward(100)
  if command == "q":
    break
    
turtle.mainloop()
turtle.bye()
```

