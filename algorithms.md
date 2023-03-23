## Algorithms: Efficiency, Analysis, and Order



#### 📌Algorithms

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

<br>

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
> 
>
> **Output**
>
> 두 행렬의 곱셈 결과를 N개의 줄에 한 줄에 한 행씩 차례대로 출력한다.

![KakaoTalk_20230318_102329978](algorithms.assets/KakaoTalk_20230318_102329978.jpg)

```cpp
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<vector<int>> matrix_t;

void multiMatrix(int n, matrix_t A, matrix_t B, matrix_t& C) {
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            for (int k = 1; k <= n; k++)
                C[i][j] += A[i][k] * B[k][j];
}

void matrixRead(int n, matrix_t& M) {
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            scanf("%d", &M[i][j]);
}

int main() {
    int n;
    scanf("%d", &n);

    matrix_t A(n+1, vector<int>(n+1));
    matrix_t B(n+1, vector<int>(n+1));
    matrixRead(n, A);
    matrixRead(n, B);

    matrix_t C(n+1, vector<int>(n+1));
    multiMatrix(n, A, B, C);

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            if (j == n)
                printf("%d\n", C[i][j]);
            else
                printf("%d ", C[i][j]);

}
```

<br>

#### 📌Five Properties

<br>

1. 입력(input)

   : 0개 이상의 외부 입력 데이터가 존재해야 한다.

2. 출력(output)

   : 하나 이상의 결과가 나와야 한다.

3. 명확성(unambiguity)

   : 모든 명령들은 모호하지 않고 단순 명확해야 한다.

4. 유한성(finiteness)

   : 한정된 수의 단계 후에 반드시 종료해야 한다.

5. 유효성(feasibility)

   : 모든 명령은 실행 가능해야 한다.

<br>

**problem ex5) - Binary Search**

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
> 만약 x*x*가 주어진 입력에 존재하지 않으면 다음과 같이 출력한다.
>
> x is not in S.

```cpp
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//이진탐색
//정렬된 array에서 해당 변수의 위치를 출력하는 알고리즘

void binsearch(int N, int x, vector<int> S, int& location) {
    int start = 1;
    int end = N;
    location = 0;

    while (start <= end) {
        int mid = (start + end) / 2;

        if (x == S[mid]) {
           location = mid;
           return; 
        }
        else if (x < S[mid])
            end = mid - 1;
        else
            start = mid + 1;

    }
}

int main() {
    int N, M;
    scanf("%d %d", &N, &M);

    vector<int> S(N+1);
    for (int i = 1; i <= N; i++)
        scanf("%d", &S[i]);

    //sort 함수
    //기본적으로 오름차순으로 정리
    //배열의 시작 주소와 마지막 주소 +1을 적으면 됨
    sort(S.begin()+1, S.end());

    for (int j = 1; j <= M; j++) {
        int x, location;
        scanf("%d", &x);
        binsearch(N, x, S, location);

        if (location == 0)
            printf("%d is not in S.\n", x);
        else
            printf("%d is in %d.\n", x, location);
    }

}
```

<br>

#### 📌Sequential Search vs Binary Search

- 최악의 경우(array에 찾고자 하는 값이 들어가있지 않은 경우), 각각의 시간 복잡도
  - sequential search : "n" comparisons
    - 처음부터 n까지 차례차례 비교해나가야 함
  - binary search : "log2(n) + 1" comparisons
    - 반띵 해나가면서 비교하기 때문에 log2(n) 만큼의 비교가 일어나고, 배열의 길이가 1만 남았을 때 남아있는 원소와 찾고자 하는 원소가 일치하는지 1 만큼의 비교 연산을 함
- array가 32개의 아이템을 가질 때, 각각의 시간 복잡도
  - sequential search : 32 comparisons
  - binary search : 6 comparisons

<br>

**problem ex6) - Fibonacci(Recursive)**

> **Description**
>
> 교재의 Algorithm 1.6. Fibonacci (Recursive) 를 재귀 버전으로 구현하시오.
>
> 이 문제에서는 피보나치 수와 함께 fib() 함수의 호출 횟수를 출력해야 한다.
>
> 단, 피보나치 수의 크기가 정수 범위를 넘어가지 않도록 다음과 같이 피보나치 수를 정의한다.
>
> F(n) = (F(n-1) + F(n-2)) % 1000000
>
> 
>
> **Input**
>
> 첫째 줄에 음이 아닌 정수 N이 주어진다. (0&lt;=*N*<=30)
>
> 
>
> **Output**
>
> 첫째 줄에 피보나치 수를 1000000 으로 나눈 나머지를 출력한다.
>
> 둘째 줄에 fib() 함수를 호출한 횟수를 출력한다.

```cpp
//fibonacci
//0은 0을, 1은 1을 출력하고
//나머지 수 f(n) = f(n-1) + f(n-2) % 1000000

#include <iostream>
using namespace std;

int cnt = 0;

int fib(int n) {
    cnt ++;

    if (n <= 1)
        return n;
    else
        return (fib(n-1) + fib(n-2)) % 1000000;
}

int main() {
    int n;
    cin >> n;

    int answer = fib(n);
    cout << answer << endl;
    cout << cnt;
}
```

<br>

Ex) ![IMG_1532](algorithms.assets/IMG_1532.jpg)

fib(5)를 실행했을 때의 값은 5이고, 재귀함수를 시행한 횟수는 총 15회이다.

=> 피보나치 알고리즘을 재귀로 구현할 경우, 상당히 **비효율적**이다. fib(5)를 계산하기 위해 fib(2)만 해도 벌써 3번을 호출했기 때문이다.

=> 같은 수를 다시 계산할 필요가 없도록, 계산 후에 array에 저장해놓으면 된다.

<br>

**problem ex7) - Fibonacci(Iterative)**

> **Description**
>
> 교재의 Algorithm 1.7. Fibonacci (Iterative) 를 반복 버전으로 구현하시오.
>
> 단, 피보나치 수의 크기가 정수 범위를 넘어가지 않도록 다음과 같이 피보나치 수를 정의한다.
>
> F(n) = (F(n-1) + F(n-2)) % 1000000
>
> 
>
> **Input**
>
> 첫째 줄에 음이 아닌 정수 N이 주어진다. (0&lt;=*N*<=10000)
>
> 
>
> **Output**
>
> 첫째 줄에 피보나치 수를 1000000 으로 나눈 나머지를 출력한다.

```cpp
#include <iostream>
#include <vector>
using namespace std;

typedef unsigned long long LongInt;

LongInt fib(int n) {
    vector<LongInt> S;
    if (n <= 1)
        return n;
    else {
        S.push_back(0);
        S.push_back(1);
        for (int i = 2; i <= n; i++)
            S.push_back((S[i-1] + S[i-2])%1000000);
        
        return S[n] % 1000000;
    }
}

int main() {
    int n;
    cin >> n;

    LongInt answer = fib(n);

    cout << answer;
}
```

<br>

**problem ex8) - 최솟값, 중앙값, 최댓값**

> **Description**
>
> 주어진 배열의 최솟값, 중앙값, 최댓값을 출력하시오.
>
> 배열의 원소 인덱스는 1부터 N까지로 가정하며, 중앙값은 [N/2] 위치에 있는 값으로 정의한다.
>
> 
>
> Algorithm 1.3 교환 정렬을 이용해도 되지만,
>
> 가급적 언어별로 제공되는 정렬 라이브러리 함수를 이용하시오.
>
> C: qsort()
>
> C++: sort()
>
> Java: Arrays.sort() 또는 Collections.sort()
>
> Python: 리스트의 sort() 메서드, 또는 sorted() 함수
>
> 
>
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
> 첫째 줄에 최솟값, 중앙값, 최댓값을 차례대로 출력한다.
>
> 배열의 원소 인덱스는 1부터 N까지로 가정하며, 중앙값은 [N/2] 위치에 있는 값으로 정의한다.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> S(n+1);
    for(int i = 1; i <= n; i++)
        cin >> S[i];

    sort(S.begin()+1, S.end());

    cout << S[1] << " " << S[(n+1)/2] << " " << S[n] << endl;
}
```

