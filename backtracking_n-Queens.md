## Backtracking - n-Queens 문제

: n * n 체스보드에 n개의 퀸을 배치하는 문제

=> 같은 행, 열, 대각선에는 다른 퀸을 놓을 수 없다.

<br>

위 문제를 풀기 위해서는 다음 퀸을 놓았을 때 유망한지 체크해야 한다.

``````
[기본 가정] 같은 행에는 퀸을 놓지 않는다.
1. 같은 열에 있는지 체크
: col(i) = col(k)
2. 대각선 체크
: |col(i) - col(k)| = |i-k|
``````

<br>

**n-Queens 문제**

> **Description**
>
> 교재와 강의자료를 참고하여n-Queens 문제를 해결하는Algorithm 5.1을 완성하시오.
>
> n의 값이 주어질 때, n-Queens 문제를 해결하는 보드의 배치가 총 몇 개인지를 카운트하고,
>
> col 배열의 값을 숫자의 문자열로 취급했을 때 가장 큰 값을 출력하도록 수정하시오.
>
> 예)
>
> n = 4일 때 가능한 보드의 배치는 다음과 같이 총 2개가 있다.
>
> col1 = [2, 4, 1, 3]
>
> col2 = [3, 1, 4, 2]
>
> 위 배치의 col 배열을 숫자의 문자열로 취급하면 각각 2413, 3142의 값을 갖는다.
>
> 따라서 이 문제의 출력은 다음과 같다.
>
> 2 ; 가능한 보드 배치의 갯수
>
> 3142 ; 가능한 보드 배치 중에서 숫자의 문자열이 가장 큰 값
>
> **Input**
>
> 첫 줄에 n의 값이 주어진다.
>
> 단, n은 4보다 크거나 같다.
>
> **Output**
>
> 첫 줄에 가능한 보드의 배치 개수를 출력한다.
>
> 둘째 줄에 col 배열의 값을 숫자의 문자열로 취급했을 때 최대값을 출력한다.
>
> **Sample Input 1**
>
> ```
> 4
> ```
>
> **Sample Output 1**
>
> ```
> 2
> 3142
> ```

```cpp
//n-Queens 문제
//행은 기본적으로 다르다고 가정하고, 열과 대각선만 유망한지 체크

#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> col; //행(row)을 나타냄. 해당 행에 배치되는 숫자는 열(col)을 나타냄.
int n, cnt;
long long maxn = -1;

bool promising(int i) {
    int k = 1;
    bool flag = true;
    while(k < i && flag) {
        if((col[i] == col[k]) || (abs(col[i] - col[k]) == i - k)) {
            flag = false;
        }
        k++;
    }
    return flag;
}

void queens(int i) {
    int j;
    if(promising(i)) {
        //i와 n이 같다는 말은 끝까지 도달했다는 말
        //promising 한데, 끝까지 왔다는 말은 출력해도 된다는 뜻이다.
        if(i == n) {
            cnt++;
            string a;
            for(int k = 1; k <= n; k++) {
                a += to_string(col[k]);
            }
            //stoll: string to long long
            if(maxn < stoll(a, NULL, 10)) {
                //maxn과 비교하여 최댓값 갱신
                maxn = stoll(a, NULL, 10);
            }
        }
        //아직 끝까지 도달 안했다면,
        //다음번에 놓을 수 있는(i+1 => 깊이가 한 단계 깊어짐) 모든 곳에 queen을 배치해본다.
        else {
            for(j = 1; j <= n; j++) {
                col[i + 1] = j;
                queens(i + 1);
            }
        }
    }
}

int main() {
    cin >> n;

    cnt = 0;
    col.resize(n + 1);

    queens(0);

    cout << cnt << "\n";
    cout << maxn;
}
```

