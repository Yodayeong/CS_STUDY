## Algorithms: Efficiency, Analysis, and Order



#### 📌Algorithms

<br>

**기본 개념들**

<br>

algorithm

> 문제를 풀기 위한 step-by-step 절차이다.

<br>

computer algorithm

> 컴퓨터를 사용해서 문제를 해결하는 명령어(instructions)의 유한집합(finite sequence)이다.

<br>

problem

> 답을 찾고자 하는 문제이다.

<br>

instance

> problem은 parameter라고 하는 변수(variable)을 가진다. 이 parameter들에 특정 값이 부여되면 이를 problem에 대한 instance라 한다. 그래서 instance는 특정 객체가 어떤 클래스의 객체인지, 관계 위주로 설명할 때 사용한다.
>
> 알고리즘 문제는 instance 집합과 output이 가져야하는 속성들이 주어지면 명시된다. 



<br><br>

**problem ex1) - Sequential Search**

> **Input**
>
> 첫째 줄에 양의 정수 N과 M이 주어진다.
>
> 둘째 줄에 N개의 양의 정수가 주어진다.
>
> 셋째 줄에 M개의 양의 정수가 주어진다.
>
> 
>
> **Output**
>
> 첫째 줄부터 한 줄에 하나씩, 입력의 셋째 줄에 주어진 양의 정수 x에 대해 아래와 같은 형식으로 위치를 출력한다.
>
> x is in location.
>
> 만약 x가 주어진 입력에 존재하지 않으면 다음과 같이 출력한다.
>
> x is not in S.

```cpp
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void seqsearch(int n, vector<int> S, int x, int& location) {
    location = 0;

    for (int i = 1; i <= n; i++)
        if (S[i] == x)
            location = i;
            return;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    vector<int> S(n+1);
    for (int i = 1; i <= n; i++)
        scanf("%d", &S[i]);

    while (m--) {
        int x, location;
        scanf("%d", &x);

        seqsearch(n, S, x, location);

        if (location > 0)
            printf("%d is in %d.\n", x, location);
        else
            printf("%d is not in S.\n", x);
    }
}
```

<br>

**problem ex2) - Adding Array Members**

> **Input**
>
> 첫째 줄에 양의 정수 N이 주어진다.
>
> 둘째 줄에 N개의 배열 원소가 주어진다.
>
> 
>
> **Output**
>
> 첫째 줄에 배열 원소의 합 S를 출력한다.

```cpp
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int sum(int n, vector<int> S) {
    int sum = 0;

    for (int i = 1; i <= n; i++)
        sum += S[i];

    return sum;
}

int main() {
    int n;
    scanf("%d", &n);

    vector<int> S(n+1);
    for (int i = 1; i <= n; i++)
        scanf("%d", &S[i]);

    printf("%d", sum(n, S));
}
```

<br>

**problem ex3) - Exchange Sort**

> **Input**
>
> 첫째 줄에 양의 정수 N이 주어진다.
>
> 둘째 줄에 N개의 양의 정수가 주어진다.
>
> 
>
> **Output**
>
> 첫째 줄에 주어진 배열 S를 오름차순으로 정렬하여 출력한다.

```cpp
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void exchange(int n, vector<int>& S) {
    int temp;
    for (int i = 1; i < n; i++)
        for (int j = i+1; j <= n; j++)
            if (S[i] > S[j]) {
                temp = S[i];
                S[i] = S[j];
                S[j] = temp;
            }
}

int main() {
    int n;
    scanf("%d", &n);

    vector<int> S(n+1);
    for (int i = 1; i <= n; i++)
        scanf("%d", &S[i]);

    exchange(n, S);

    for (int i = 1; i <= n; i++)
        printf("%d ", S[i]);
}
```

<br>

**problem ex4) - Matrix Multiplication**

> **Input**
>
> 첫째 줄에 양의 정수 N이 주어진다.
>
> 다음 줄부터 N개의 줄에 첫 번째 N*N 행렬의 원소가 한 줄에 한 행씩 차례대로 주어진다.
>
> 다음 줄부터 N개의 줄에 두 번째 N*N 행렬의 원소가 한 줄에 한 행씩 차례대로 주어진다.
>
> 
>
> **Output**
>
> 두 행렬의 곱셈 결과를 N개의 줄에 한 줄에 한 행씩 차례대로 출력한다.

![KakaoTalk_20230318_102329978](algorithms.assets/KakaoTalk_20230318_102329978.jpg)

```cpp
```

