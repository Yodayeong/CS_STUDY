#binary search 시험에 낼 수도 있으니 공부할것 !
#내가 짠 코드인데 약간 이상하니 찾아보삼

def binary_search(n, sorted_list, start, end):
    mid = (start + end) // 2
    if sorted_list[mid] == n:
        print(mid)
        return 0
    elif sorted_list[mid] < n:
        binary_search(n, sorted_list, mid + 1, end)
    else:
        binary_search(n, sorted_list, start, mid - 1)

n = int(input("찾고 싶은 숫자를 입력해주세요: "))
sorted_list = [1, 2, 3, 4, 5, 6]
binary_search(n, sorted_list, 0, len(sorted_list) - 1)


#튜플
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


numbers = 1, 2, 3
print(numbers, type(numbers)) #(1, 2, 3) <class 'tuple'>
a, b, c = numbers
print(a, type(a)) #1