#tuple, set, dictionary

#binary search 시험에 낼 수도 있으니 공부할것 !
#내가 짠 코드인데 약간 이상하니 찾아보삼

def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return

n = int(input())
sorted_list = [1, 2, 3, 4, 5, 6]
print(binary_search(n, sorted_list))


#1. 튜플
#=> element를 바꿀 수 없음

composer = ("Bach", "Beethoven", "Brahms")
print(composer) #('Bach', 'Beethoven', 'Brahms')
print(composer[0]) #Bach

composer_ = ["Bach", "Beethoven", "Brahms"]
print(composer_[0]) #Bach

composer_[0] = "Wagner"
print(composer_)

# composer[0] = "Wagner"
# print(composer)
#=> 튜플도 인덱싱, 슬라이싱은 되지만, element를 바꿀 수는 없음
#=> 리스트는 mutable, 튜플은 immutable. 이게 가장 큰 차이점.


#packing을 통해 튜플을 만듬
numbers = 1, 2, 3
print(numbers, type(numbers)) #(1, 2, 3) <class 'tuple'>

#unpacking
a, b, c = numbers
print(a, type(a)) #1 <class 'int'>

singers = ("Michael Jackson")
print(type(singers)) #<class 'str'>
#=> 이때의 괄호는 튜플을 나타내는게 아니라, 우선순위를 나타냄

great_singers = ("Michael Jackson", ) #<class 'tuple'>
print(type(great_singers))
#=> 이때는 튜플로 생성됨

#빈 튜플 생성
rockBands = ()
print(type(rockBands)) #<class 'tuple'>

#값 추가
# rockBands[0] = "Queen"
#=> 튜플에 위처럼 값추가 안됨

#리스트와 튜플은 왔다갔다 할 수 있음
list_ = list(range(1, 8))
print(list_) #[1, 2, 3, 4, 5, 6, 7]

tuple_ = tuple(list_)
print(tuple_) #(1, 2, 3, 4, 5, 6, 7)

numbers_ = list(numbers)
print(numbers_) #[1, 2, 3]
print(numbers) #(1, 2, 3)

rockBands_ = list(rockBands)
print(rockBands_) #[]

#반복문을 통해 요소 출력
#=> 선형구조여서
for c in composer:
    print(c)
# Bach
# Beethoven
# Brahms

for index, value in enumerate(composer):
    print(index, value)
# 0 Bach
# 1 Beethoven
# 2 Brahms


#2. set(집합)
#=> multiple items를 single variable에 저장한다.
#=> unordered, unchangeable, unindexed
thisset = {"apple", "banana", "cherry"}
print(thisset) #{'cherry', 'banana', 'apple'}

thisset.add("orange")
print(thisset) #{'apple', 'orange', 'cherry', 'banana'}

#set 생성
classic_composers = {}
print(type(classic_composers)) #<class 'dict'>
#=> set으로 생성이 안 됨

ccomposers = set()
print(type(ccomposers)) #<class 'set'>

list_ = [0, 1, 2, 1, 2, 3, 2, 1, 0]
set_ = set(list_)
print(type(set_)) #<class 'set'>
print(set_) #{0, 1, 2, 3} 
#=> set은 중복 제거

list_selected = []

for l in list_:
    if l not in list_selected:
        list_selected.append(l)
print(list_selected) #[0, 1, 2, 3]

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset) #{'cherry', 'apple', 'pineapple', 'papaya', 'mango', 'banana'}

thisset.discard("pineapple")
print(thisset) #{'mango', 'banana', 'papaya', 'cherry', 'apple'}

#join
#=> 합집합
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) #{1, 2, 3, 'a', 'c', 'b'}

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")
    
    
#3. dictionary
#=> key, value로 구성

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict["brand"]) #Ford

x = thisdict.keys()
print(x) #dict_keys(['brand', 'model', 'year'])
x = thisdict.values() #dict_values(['Ford', 'Mustang', 1964])
print(x)

thisdict["car"] = "hello"
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'car': 'hello'}

#items
#return each item in a dictionary as tuples in a list
x = thisdict.items() #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('car', 'hello')])
print(x)