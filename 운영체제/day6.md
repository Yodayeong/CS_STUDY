function

```python
def greet(name):
    print("Hello, " + name + "! How are you?")
    
greet("John")
greet("Sam")
```

=> 코드를 재사용할 수 있음

```python
def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 ==0:
            even_numbers.append(number)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)
```

<br>

function(함수)란?

- 특정 작업을 수행하는 명령어들의 모음에 이름을 붙인 것

<br>

예제

```python
def get_area(radius):
    area = 3.14*radius**2
    return area

result = get_area(3)
print("반지름이 3인 원의 면적=", result)
```

<br>

여러 개의 값 반환하기

```python
def get_input():
    return 2, 3

x, y = get_input()
print(x, y)
```

<br>

예전에 한 거

```python
x = 2
y = 3
x, y = y, x

print(x, y)
```

<br>

함수의 순서

- 파이썬은 인터프리트 언어이기 때문에 함수의 순서가 중요하다.

  ```python
  def main():
    #함수 안에서는 정의되지 않은 함수를 호출 가능하다. main이 젤 아래에 있어서
      result1 = get_area(3)
      print("반지름이 3인 원의 면적=", result1)
      
  def get_area(radius):
      return 3.14*radius**2
      
  main()
  ```

<br>

예제

```python
def main():
    print("20cm 피자 2개의 면적:", get_area(20) + get_area(20))
    print("30cm 피자 1개의 면적:", get_area(30))
    
## 원의 면적을 계산한다.
# @param radius 원의 반지름
# @return 원의 면적

def get_area(radius):
    if radius > 0:
        area = 3.14*radius ** 2
    else:
        area = 0
    return area

main()
```

<br>

서로 다른 인수로 호출될 수 있다.

```python
def get_sum(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum

#1과 10이 get_sum()의 인수가 된다.
x = get_sum(1, 10)

#1과 20이 get_sum()의 인수가 된다.
y = get_sum(1, 20)

print(x, y)
```

=> positional parameter(위치에 따라 처리 됨)

<br>

디폴트 인수

```python
def greet(name, msg="별일없죠?"):
    print("안녕 " + name + ", " + msg)
    
greet("영희") #안녕 영희, 별일없죠?
greet("영희", "안녕하세요?") #안녕 영희, 안녕하세요?
```

=> 매개변수에 값을 주지 않으면 기본값 출력

<br>

키워드 인수

```python
def sub(x, y, z):
    print("x=", x, "y=", y, "z=", z)
    
sub(10, 20, 30)
sub(x=10, y=20, z=30)
sub(10, y=20, z=30)
sub(x=10, z=30, y=20)
sub(x=10, 20, 30 ) #SyntaxError: positional argument follows keyword argument
```

=> 인수의 이름을 명시적으로 지정해서 값을 매개 변수로 전달하는 방법이다.

<br>

가변 함수

```python
def varfunc(*args):
    print(args)
    
print("하나의 값으로 호출")
varfunc(10)

print("여러 개의 값으로 호출")
varfunc(10, 20, 30)

#======
def add(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print(add(10, 20))
print(add(10, 20, 30))
```

<br>

매개 변수 이름 앞에 이중별표를 이용해 가변 길이를 나타냄

```python
def myfunc(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    return result

print(myfunc(a="Hi!", b="Mr.", c="Kim"))
```

<br>

예제

```python
alist = [1, 2, 3]
print(*alist) #1 2 3

alist = [1, 2, 3]
print(alist) #[1, 2, 3]

#=====
def sum(a, b, c):
    print(a + b + c)
    
alist = [1, 2, 3]
sum(*alist)
```

=> * 연산자로 리스트 구조 언패킹. **는 딕셔너리 구조를 언패킹

<br>

환영 문자열 출력 함수

```python
def display(ms, count=1):
    for k in range(count):
        print(msg)
        
display("환영합니다.", 5)
```

<br>

함수를 사용하는 이유

- 소스 코드의 중복성을 없애준다.