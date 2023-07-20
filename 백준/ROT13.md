## [백준 / 11655] ROT13

> ## 문제
>
> ROT13은 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.
>
> 예를 들어, "Baekjoon Online Judge"를 ROT13으로 암호화하면 "Onrxwbba Bayvar Whqtr"가 된다. ROT13으로 암호화한 내용을 원래 내용으로 바꾸려면 암호화한 문자열을 다시 ROT13하면 된다. 앞에서 암호화한 문자열 "Onrxwbba Bayvar Whqtr"에 다시 ROT13을 적용하면 "Baekjoon Online Judge"가 된다.
>
> ROT13은 알파벳 대문자와 소문자에만 적용할 수 있다. 알파벳이 아닌 글자는 원래 글자 그대로 남아 있어야 한다. 예를 들어, "One is 1"을 ROT13으로 암호화하면 "Bar vf 1"이 된다.
>
> 문자열이 주어졌을 때, "ROT13"으로 암호화한 다음 출력하는 프로그램을 작성하시오.
>
> ## 입력
>
> 첫째 줄에 알파벳 대문자, 소문자, 공백, 숫자로만 이루어진 문자열 S가 주어진다. S의 길이는 100을 넘지 않는다.
>
> ## 출력
>
> 첫째 줄에 S를 ROT13으로 암호화한 내용을 출력한다.
>
> ## 예제 입력 1 
>
> ```
> Baekjoon Online Judge
> ```
>
> ## 예제 출력 1 
>
> ```
> Onrxwbba Bayvar Whqtr
> ```

<br>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string sentence;
    getline(cin, sentence);
    
    for(int i = 0; i <= sentence.length(); i++) {
        char c = sentence[i];
        //소문자인 경우
        if(c >= 'a' && c <= 'z') {
            c -= 'a'; //'a'를 빼서 c를 0 ~ 25 사이 수로 맞춰준다.
            c += 13; //알파벳 13글자를 민다.
            c %= 26; //소문자 총 26자이므로, 26으로 나눈 나머지를 저장한다.
            c += 'a'; //다시 'a'를 더해, 알파벳으로 변환한다.
        }
        //대문자인 경우
        else if(c >= 'A' && c <= 'Z') {
            c -= 'A'; //'A'를 빼서 c를 0 ~ 25 사이 수로 맞춰준다.
            c += 13; //알파벳 13글자를 민다.
            c %= 26; //대문자 총 26자이므로, 26으로 나눈 나머지를 저장한다.
            c += 'A'; //다시 'A'를 더해, 알파벳으로 변환한다.
        }
        sentence[i] = c;
    }
    cout << sentence << endl;
}
```

