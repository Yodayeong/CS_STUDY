#1. locals()
#=> 현재 지역 스코프의 로컬 심볼 테이블을 나타내는 딕셔너리를 반환하는 파이썬 내장 함수이다.
#=> 이 딕셔너리는 지역 변수들과 그들의 값들을 포함합니다.

def example_function():
    a = 10
    b = "Hello"
    c = [1, 2, 3]

    local_variables = locals()

    # 지역 변수들의 딕셔너리 출력
    print("Local Variables:", local_variables)

    # 특정 지역 변수 값에 접근
    print("Value of 'a':", local_variables.get('a'))

example_function()



#2. getattr(object, name) / getattr(object, name, default)
#=> 객체(object)의 속성(attribute) 값을 가져오는 함수이다.

class ExampleClass:
    def __init__(self):
        self.attribute1 = 42
        self.attribute2 = "Hello, World!"

# ExampleClass 인스턴스 생성
example_instance = ExampleClass()

# getattr() 함수를 사용하여 속성 값 가져오기
value1 = getattr(example_instance, 'attribute1', None)
value2 = getattr(example_instance, 'attribute2', None)
value3 = getattr(example_instance, 'attribute3', 'Default Value')

# 결과 출력
print("Value of attribute1:", value1)
print("Value of attribute2:", value2)
print("Value of attribute3:", value3)



#3. delattr(object, name)
#=> 객체(object)의 속성(attribute)을 삭제하는 함수이다.

class ExampleClass:
    def __init__(self):
        self.attribute1 = 42
        self.attribute2 = "Hello, World!"

# ExampleClass 인스턴스 생성
example_instance = ExampleClass()

# 객체의 속성 삭제하기
print("Before deleting attribute1:", hasattr(example_instance, 'attribute1'))

delattr(example_instance, 'attribute1')

# 삭제 후 확인
print("After deleting attribute1:", hasattr(example_instance, 'attribute1'))