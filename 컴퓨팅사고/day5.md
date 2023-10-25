리스트

- `singers = [ ]`
- `singers = [ "BTS", "Blank Pink", "Beatles", "Coldplay" ]`
- `len(singers)`
- => 순차적으로 나타나는 데이터를 담는 새로운 데이터 타입 list

<br>

range함수 시험

- `range(start, stop, step)`
- 필수로 들어가야 하는 건 stop 값
- `range(3), range(1, 3), range(1, 3, 2)`의 차이를 설명할 줄 알아야 한다.

<br>

리스트

```
singers = [ "BTS", "Black Pink", "Beatles", "Coldplay" ]

for i in range(len(singers)):
    print(singers[i])
    
for singer in singers:
    print(singer)
    
singers.append("Queen")

print(len(singers)) #5
print(singers[-1]) #Queen

singers.insert(2, "New Jeans")

print(singers) #['BTS', 'Black Pink', 'New Jeans', 'Beatles', 'Coldplay', 'Queen']
print(singers.pop(1)) #Black Pink
print(len(singers)) #5

singers.remove('BTS')
print(singers)

singers.sort()
print(singers)

singers.sort(reverse=True)
print(singers)
```

<br>리스트: 다양한 형태의 데이터

- `compound_data = ["Tom", 123, 2,]`

<br>

Slicing

```python
singers = ["BTS", "Balck Pink", "뉴진스", "Beatles", "Coldplay", "아이유", "Queen", "Michael Jackson"]
num_singers = len(singers)

print(singers) #['BTS', 'Balck Pink', '뉴진스', 'Beatles', 'Coldplay', '아이유', 'Queen', 'Michael Jackson']
print(singers[len(singers) - 1]) #Michael Jackson

#singers[::] => start, stop, step
print(singers[:]) #['BTS', 'Balck Pink', '뉴진스', 'Beatles', 'Coldplay', '아이유', 'Queen', 'Michael Jackson']
print(singers[3:5]) #['Beatles', 'Coldplay']
print(singers[::2]) #['BTS', '뉴진스', 'Coldplay', 'Queen']
print(singers[::-1]) #['Michael Jackson', 'Queen', '아이유', 'Coldplay', 'Beatles', '뉴진스', 'Balck Pink', 'BTS']
print(singers[-3:]) #['아이유', 'Queen', 'Michael Jackson']

status_ = "stressed"
status = status_[::-1]
print(status)
```

<br>

펠린드롬인지 확인하기

```python
#펠린드롬인지 확인하기
def pelindrom(word_, word_reverse):
    if word_ == word_reverse:
        print("펠린드롬입니다.")
    else:
        print("펠린드롬이 아닙니다.")

word_ = input()
word_reverse = word_[::-1]

pelindrom(word_, word_reverse)
```

<br>

Slicing

```python
list1 = [1, 2, 3]
list_ = list1 * 3
print(list_) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

list2 = [4, 5, 6]
list_ = list1 + list2
print(list_) #[1, 2, 3, 4, 5, 6]

#=======
letters = ['a', 'b', 'c', 'd', 'e']

letters[2:5] = []
print(letters) #['a', 'b']

#=======
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print(x) #[['a', 'b', 'c'], [1, 2, 3]]
print(x[0]) #['a', 'b', 'c']
print(x[0][1]) #b
```

<br>

피보나치 수열

```python
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b
```

<br>

리스트

```python
squares = [x**2 for x in range(10)]
print(squares) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares) #[0, 4, 16, 36, 64]
```

<br>

Salary

```python
salary = [100, 200, 300, 400]

def modify(values, factor):
    for i in range(len(values)):
        values[i] = values[i] * factor
        
print("before merit increase : ", salary)
modify(salary, 1.2)
print("after merit increase : ", salary)
```

<br>

시험(함수로 구현하는 법)

- 소수찾기
- 피보나치
- 팩토리얼
- 숫자 덧셈