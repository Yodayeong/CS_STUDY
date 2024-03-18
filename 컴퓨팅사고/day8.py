#https://realpython.com - tutorial이 많이 올라옴. 공부할 때 참고.
#Learn Python -> Quizzes

#Lists and Tuples: https://realpython.com/quizzes/python-lists-tuples/
#=> 시험 이런 식으로 나올수도

#딕셔너리
#키(key)- 값(value)로 저장
capitals = {
    "Korea": "Seoul",
    "USA": "Washington",
    "UK": "London"
}

print(capitals)

#딕셔너리는 key 값으로 접근
print(capitals["Korea"])
print(capitals.get("Korea"))

# print(capitals["France"]) #에러
print(capitals.get("France")) #None

print(dir(capitals))

#help() => built in 되어있는 help
# help(dir)

# help(capitals) #capitals가 해당 되는 datatype이 쓸 수 있는 메서드들을 보여줌

#값 추가
capitals["France"] = "Paris"
print(capitals)

#값 삭제 - pop 메서드 사용
city = capitals.pop("UK")
print(city, type(city)) #London <class 'str'>

if "UK" in capitals:
    capitals.pop("UK")
    
#dictionary 항목 방문하기
for key in capitals:
    print(key, ":", capitals[key])

#items
for key, value in capitals.items():
    print(f"{key} : {value}")
    
#key값만 가지고 옴
for key in capitals.keys():
    print(key)
#dict_key 타입으로 반환

for value in capitals.values():
    print(value)
#dict_values 타입으로 반환

#딕셔너리 함축
values = [1, 2, 3, 4, 5, 6]
dic = {x: x**2 for x in values if x % 2 == 0}
print(dic)

#객체지향 프로그래밍(Object-Oriented-Programming)
#서로 관련 있는 데이터와 함수를 묶어서 객체(object)를 만들고,
#이들 객체들이 모여서 하나의 프로그램이 된다.

#Class => 객체에 대한 설계도
#ex) Class:Car - Object:철수 자동차, 영희 자동차, 길동 자동차
class Cat:
    #생성자
    #객체가 생성될 때, 자동으로 생성되도록 하는 constructor
    #default parameter => 정의가 안되있으면, default parameter로 값 설정
    def __init__(self, name, color="Black"):
        self.name = name
        self.color = color
    
    def meow(self):
        print("야옹 야옹")
    
    def __str__(self):
        return '{%s}' % self.name

cat = Cat("Neo", "Yellow")
print(cat.name, cat.color)
cat.meow()
print(cat.__str__)

#Counter 클래스
class Counter:
    def __init__(self, initValue=0):
        self.count = initValue
    def increment(self):
        self.count += 1

a = Counter()
print(a.count)
a.increment()
print(a.count)
b = Counter(100)
print(b.count)

#TV 클래스
class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
    
    def show(self):
        print(self.channel, self.volume, self.on)
        
    def setChannel(self, channel):
        self.channel = channel

    def getChannel(self):
        return self.channel

#Circle 클래스
import math
class Circle:
    def __init__(self, radius = 0):
        self.radius = radius
    
    def getArea(self):
        return math.pi * self.radius * self.radius
    
    def getPerimeter(self):
        return 2 * math.pi * self.radius

c = Circle(10)
print("원의 면적", c.getArea())
print("원의 둘레", c.getPerimeter())

#캡슐화
#공용 인터페이스만 제공하고 구현 세부 사항을 감추는 것

#정보 은닉
#인스턴스 변수를 private으로 정의하려면, 변수 이름 앞에 __을 붙이면 된다.
#private이 붙은 인스턴스 변수는 클래스 내부에서만 접근될 수 있다.
class Student:
    def __init__(self, name=None, age=0):
        self.__name = name #외부에서 변경 금지
        self.__age = age #외부에서 변경 금지
    
    #접근자와 설정자
    #외부에서는 getter와 setter를 통해서만 값을 가져오거나 변경 가능
    def getAge(self):
        return self.__age
    
    def getName(self):
        return self.__name
    
    def setAge(self, age):
        self.__age = age
        
    def setName(self, name):
        self.__name = name
        
obj = Student()
print(obj.getAge()) #0

obj.setAge(10)
print(obj.getAge()) #10

# print(obj.__name) #AttributeError: 'Student' object has no attribute '__name' => 변수에 접근 자체가 불가능

#Bank Account 클래스
class Bank_Account:
    def __init__(self, balance = 0):
        self.balance = balance
    
    def deposit(self, amount = 0):
        self.balance += amount
        print(f"통장에서 {amount}가 입금되었음")
        
    def withdraw(self, amount = 0):
        self.balance -= amount
        print(f"통장에서 {amount}가 출금되었음")

bank_account = Bank_Account(500)
bank_account.withdraw(100)
bank_account.deposit(10)
print(bank_account.balance)

#참조 공유
t = Television(11, 10, True)
s = t
s.channel = 9
print(t.channel) #9
print(s.channel) #9

#클래스 변수
#모든 객체를 통틀어서 하나만 생성되고 모든 객체가 이것을 공유하는 변수
class TV:
    serialNumber = 0 #클래스 변수
    
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
        TV.serialNumber += 1 #각 객체마다 다른 serialNumber를 가지게 됨
        self.number = TV.serialNumber #serialNumber를 객체의 number로 지정
        
#특수 메소드
#연산자(+, -, *, /)에 관련된 특수 메소드
#이들 메소드는, 우리가 객체에 대하여 +, -, *, /와 같은 연산을 적용하면 자동으로 호출된다.
class Circle:
    def __init__(self, radius=0):
        self.radius = radius
    
    def __eq__(self, other):
        return self.radius == other.radius
    
c1 = Circle(10)
c2 = Circle(10)
if c1 == c2:
    print("원의 반지름은 동일합니다.")

#주사위 클래스
import random
class Dice:
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.size = 30
        self.value = 1
    
    def roll_dice(self):
        self.value = random.randint(1, 6)
    
    def read_dice(self):
        print(f"value: {self.value}")
    
dice = Dice(1, 2)
print(dice.roll_dice())
print(dice.read_dice)

#Person 클래스
class Person:
    def __init__(self, name, mobile, email):
        self.__name = name
        self.__mobile = mobile
        self.__email = email
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
        
    def getMobile(self):
        return self.__mobile
    
    def setMobile(self, mobile):
        self.__mobile = mobile
    
    def getEmail(self):
        return self.__email
    
    def setEmail(self, email):
        self.__email = email
        
    def __str__(self):
        return '이름: {}, 폰번호: {}, 이메일: {}'.format(self.__name, self.__mobile, self.__email)
        
person = Person("여다영", "010-1111-2222", "1111@naver.com")
print(person)
    
#PhoneBook 딕셔너리
PhoneBook = dict()

PhoneBook["여다영"] = ("010-1111-2222", "1111@naver.com")
PhoneBook["이이이"] = ("010-1111-3333", "2222@naver.com")

print(PhoneBook)