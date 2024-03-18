#SWEA 1240

#암호코드는 8개의 숫자
#올바른 암호코드는 (홀수 자리 합 * 3) + (짝수 자리 합)이 10의 배수

#암호코드 1개가 포함된 직사각형 배열
#암호코드 이외의 부분은 전부 0
#암호코드에서 숫자 하나는 7개의 비트로 암호화되어 주어진다,
#따라서 암호코드의 가로길이는 56이다.

#암호코드 정보가 포함된 2차원 배열을 입력받아, 올바른 암호코드인지 판별

def find_out(now):
    for d in decode:
        if now == d:
            return decode[d]
        
def check(numbers):
    sum_i = sum_j = 0
    for i in range(0, len(numbers), 2):
        sum_i += numbers[i]
    for j in range(1, len(numbers), 2):
        sum_j += numbers[j]
        
    if (sum_i * 3 + sum_j) % 10 == 0:
        return sum_i + sum_j
    else:
        return 0

T = int(input())
decode = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

for tc in range(T):
    n, m = map(int, input().split())
    matrix = [list(input().split()) for _ in range(n)]
    
    for m in matrix:
        now = str(m[0])
        for i in range(len(now)):
            if now[i] == '1':
                code = now
    
    for i in range(len(m[0]) - 1, -1, -1):
        if code[i] == "1":
            here = i
            break
    
    final_code = ""
    for i in range(here, here-56, -1):
        final_code += code[i]
        
    final_code = final_code[::-1]

    # print(final_code, len(final_code))
    numbers = []
    for i in range(0, len(final_code), 7):
        now = final_code[i:i + 7]
        numbers.append(find_out(now))
    # print(numbers)
    
    print(f"#{tc + 1} {check(numbers)}")