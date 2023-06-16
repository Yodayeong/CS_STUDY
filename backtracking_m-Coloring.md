## Backtracking - m-Coloring 문제

그래프의 정점을 m개의 색으로 칠하는 문제

<br>

``````
재귀: 한 정점을 선택하고 해당 정점에 색상 할당 후, 다음 정점으로 재귀호출 
promising: 이때, 인접한 정점과의 색상 충돌을 체크하여 색상이 할당 가능한지 확인
``````

<br>

**m-Coloring 문제**

> **Description**
>
> 교재와 강의자료를 참고하여 m-Coloring 문제를 해결하는 Algorithm 5.5의 구현은 완성하시오.
>
> 주어진 평면 그래프 G = (V, E)에 대해서
>
> 인접한 지역을 서로 다른 색으로 색칠하기 위해 필요한 최소 색의 수 m의 값과
>
> 해당하는 m의 값으로 색칠할 수 있는 경우의 수를 출력하시오.
>
> 단,그래프의 입력은 간선의 집합으로 주어지고,주어진 그래프는 평면 그래프라고 가정해도 된다.
>
> **Input**
>
> 첫 줄에 정점의 수 n과 간선의 수 k가 주어진다.
>
> 둘째 줄부터 k개의 간선이 주어진다.
>
> **Output**
>
> 첫째 줄에 색칠 가능한 최소의 m값을 출력한다.
>
> 둘째 줄에 해당 m값으로 색칠할 수 있는 경우의 수를 출력한다.
>
> **Sample Input 1**
>
> ```
> 4 5
> 1 2
> 1 3
> 1 4
> 2 3
> 3 4
> ```
>
> **Sample Output 1**
>
> ```
> 3
> 6
> ```

```cpp
//m-Coloring 문제
//인접한 노드의 색상을 체크 후, 적절한 색상을 배치하는 문제

#include <iostream>
#include <vector>

using namespace std;
vector<vector<int>> W; //간선체크
vector<int> vcolor;
int n, k;
int cnt = 0, m = 1; //m은 색칠가능한 최소의 색상 수, cnt는 m으로 색칠할 수 있는 경우의 수

bool promising(int i) {
    int j = 1;
    bool flag = true;
    while(j < i && flag) {
        if(W[i][j] && vcolor[i] == vcolor[j]) {
            flag = false;
        }
        j++;
    }
    return flag;
}

void m_coloring(int i) {
    int color;
    if(promising(i)) {
        if(i == n) {
            cnt++;
            /*
            for(int j = 1; j <= n; j++) {
                cout << vcolor[j] << " ";
            }
            cout << "\n";
            */
        }
        else {
            for(color = 1; color <= m; color++) {
                vcolor[i + 1] = color;
                m_coloring(i + 1);
            }
        }
    }
}

int main() {
    cin >> n >> k;

    vcolor.resize(n + 1);
    W.resize(n + 1);
    for (int i = 0; i <= n; i++)
    {
        W[i].resize(n + 1);
    }

    for (int i = 0; i < k; i++)
    {
        int a = 0, b = 0;
        cin >> a >> b;

        //간선 체크
        W[a][b] = 1;
        W[b][a] = 1;
    }

    while(1) {
        //cnt가 0이 아니라 정수가 나올때까지
        //m을 증가시켜가면서, 0번째 노드부터 m_coloring을 무한반복
        m_coloring(0);

        if(cnt != 0) {
            break;
        }
        m++;
    }
    cout << m << "\n" << cnt;
}
```

