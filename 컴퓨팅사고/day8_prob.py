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

print(person.getName())
    
#PhoneBook 딕셔너리
PhoneBook = dict()

#삽입
PhoneBook["여다영"] = ("010-1111-2222", "1111@naver.com")
PhoneBook["이이이"] = ("010-1111-3333", "2222@naver.com")
print(PhoneBook)

#삭제
PhoneBook.pop("여다영")
print(PhoneBook)

#특정 key 접근
print(PhoneBook["이이이"])