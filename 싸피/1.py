#SWEA 2050

#ord(), chr()함수를 통해 문자를 아스키코드로, 아스키코드를 문자로!

word_ = input()

for w in word_:
    print(ord(w) - 64, end=" ")