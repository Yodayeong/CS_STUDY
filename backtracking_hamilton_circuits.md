## Backtracking - 해밀턴 회로 문제

그래프에서 모든 정점을 한 번씩 방문하고 시작 정점으로 돌아오는 경로를 찾는 문제

(이때, 간선을 중복해서 지나지 않아야 함)

<br>

``````
재귀: 한 정점을 선택하고 해당 정점을 방문한 후, 다음 정점으로 재귀 호출
promising: 이때, 방문한 정점을 체크하고 중복 방문을 방지
``````

<br>

**해밀턴 회로 문제**

> **Description**
>
> 교재와 강의자료를 참고하여 해밀턴 회로 문제를 해결하는 Algorithm 5.6의 구현을 완성하시오.
>
> 주어진 무방항 무가중치 그래프 G = (V, E) 에서
>
> 해밀턴 회로의 개수를 출력하시오.
>
> Algorithm 5.6을 구현할 때, 출발정점은 1로 간주한다는 것을 주의하시오.
>
> vindex[0] = 1;
>
> hamiltonian(0);
>
> **Input**
>
> 첫째 줄에 정점의 개수 n과 간선의 개수 m이 주어진다.
>
> 둘째 줄부터 m개의 간선이 주어진다.
>
> **Output**
>
> 첫째 줄에 해밀턴 회로의 개수를 출력한다.
>
> **Sample Input 1**
>
> ```
> 8 13
> 1 2
> 1 3
> 1 7
> 1 8
> 2 3
> 2 7
> 2 8
> 3 4
> 3 6
> 4 5
> 5 6
> 6 7
> 7 8
> ```
>
> **Sample Output 1**
>
> ```
> 8
> ```

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> W;
vector<int> vindex; //정점들의 순서를 나타내는 배열
int n, m;
int cnt = 0;

bool promising(int i) {
    int j;
    bool flag;
    //1. i가 마지막 정점이지만, 첫번째 정점과 연결되어 있지 않은 경우
    if(i == n - 1 && !W[vindex[n - 1]][vindex[0]])
        flag = false;
    //2. i가 0보다 크고, 이전 정점과 현재 정점이 연결되어 있지 않은 경우
    //non-promising 하다.
    else if(i > 0 && !W[vindex[i - 1]][vindex[i]])
        flag = false;
    //그렇지 않은 경우,
    else {
        flag = true;
        j = 1;
        while(j < i && flag) {
            //중복 방문한 노드가 있다면,
            //non-promising 하다.
            if(vindex[i] == vindex[j])
                flag = false;
            j++;
        }
    }
    return flag;
}

void hamilton(int i) {
    int j;
    if(promising(i)) {
        if(i == n - 1) {
            cnt++;
            /*
            for(int i = 0; i <= n - 1; i++) {
                cout << vindex[i] << " ";
            }
            cout << "\n";
            */
        }
        else {
            for(j = 2; j <= n; j++) {
                vindex[i + 1] = j;
                hamilton(i + 1);
            }
        }
    }
}

int main() {
    cin >> n >> m;
    
    W.resize(n + 1);
    vindex.resize(n + 1);

    for(int i = 0; i <= n; i++) {
        W[i].resize(n + 1);
    }
    
    for(int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;

        W[a][b] = 1;
        W[b][a] = 1;
    }

    vindex[0] = 1;

    hamilton(0);

    cout << cnt;
}
```
