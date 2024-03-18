#내장함수
#파이썬 인터프리터에는 항상 사용할 수 있는 많은 함수가 준비
#ex) int(), min(), abs(), input(), sum(), print()

#https://docs.python.org/3/library/functions.html

#all() 함수
#=> 시퀀스의 모든 항목이 참이면 True 반환

#any() 함수
#=> 시퀀스의 한 개의 항목이라도 참인 경우 True 반환

#eval() 함수
#=> 전달된 수식을 구문 분석하고, 프로그램 내에서 수식 실행
x = 10
print(eval('x + 1'))

#map() 함수
#=> 반복가능한 객체(리스트, 튜플 등)의 각 항목에 주어진 함수를 적용한 후, 결과를 반환
def square(n):
    return n * n

mylist = [1, 2, 3, 4, 5]
result = list(map(square, mylist))
print(result)

#dir() 함수
#=> 객체가 가지고 있는 변수나 함수를 보여 준다.
print(dir([1, 2, 3]))

#enumerate() 함수
#=> 시퀀스 객체를 입력 받아, 열거형(enumerate) 객체를 반환
seasons = ["Spring", "Summer", "Fall", "Winter"]

print(list(enumerate(seasons)))
print(list(enumerate(seasons, start = 1)))

for index, season in enumerate(seasons):
    print(f"Index {index}: {season}")
    
#lambda => reserved word
#=> 한 번 사용하고 버리는 함수. 특정 목적으로 내가 설계한 함수
#map(lambda x: x * x, )

f = lambda x, y: x + y
print(f(2, 3))

list_ = [3, 6, 9, 12, 14, 17, 19, 21, 24]
result = list(map(lambda x: x if x % 3 == 0 else 0, list_))
print(result)

#filter() 함수
#=> 특정 조건을 만족하는 요소만을 뽑는다.
def myfilter(x):
    return x > 3

result = filter(myfilter, (1, 2, 3, 4, 5, 6))
print(list(result))

#zip() 함수
#=> 2개의 자료형을 하나로 묶어주는 함수
numbers = [1, 2, 3, 4]
slist = ["one", "two", "three", "four"]

print(list(zip(numbers, slist)))

#reduce() 함수와 람다식
#=> reduce(func, seq) 함수는 func() 함수를 시퀀스 seq에 연속적으로 적용하여, 단일 값을 반환

#Lab: 람다식으로 온도 변환하기
def celsius(T):
    return (5.0/9.0) * (T - 32.0)

f_temp = [0, 10, 20, 30, 40, 50]

c_temp = map(celsius, f_temp)
print(list(c_temp))

#이터레이터
#=> __iter__()은 이터러블 객체 자신을 반환한다.
#=> __next__()은 다음 반복을 위한 값을 반환. 만약 더 이상의 값이 없으면, StopIteration 예외를 발생하면 된다.
class MyCounter(object):
    #생성자 메서드를 정의한다.
    def __init__(self, low, high):
        self.current = low
        self.high = high
        
    #이터레이터 객체로서 자신을 반환한다.
    def __iter__(self):
        return self
    
    def __next__(self):
        #current가 high보다 크면 StopIteration 예외를 발생시킨다.
        #current가 high보다 작으면 다음 값을 반환한다.
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

#=> 피보나치
class FibonacciGenerator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
        self.next_value = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        else:
            result = self.current
            self.current, self.next_value = self.next_value, self.current + self.next_value
            return result

fibonacci_limit = 50
fibonacci_gen = FibonacciGenerator(fibonacci_limit)

for value in fibonacci_gen:
    print(value)

#연산자 오버로딩
#=> 연산자를 메서드로 정의하는 것

#TEST
#Class Point 부분에 add dunder 생성하는 것

import calendar

cal = calendar.month(2016, 8)
print(cal)

#파이썬 package 3개 조사하고,
#뭔지, 어떻게 활용 되는지, 샘플코드
#워드문서, .py로 작성

#ex) pandas