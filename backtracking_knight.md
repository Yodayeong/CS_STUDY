## Backtracking - 기사의 여행 문제와 해밀턴 경로

n * m 체스보드에서 knight가 모든 지역을 반드시 한번씩만 방문하는 ''경로(시작 노드로 되돌아오지 X)' / '회로(시작 노드로 되돌아오는)' 찾기

<br>

무방향 그래프 G = (V, E)가 주어질 때, 임의의 정점에서 출발하여 간선을 따라 모든 정점을 한 번만 방문하고,

(회로) 출발 정점으로 되돌아오는 사이클

(경로) 출발 정점으로 되돌아 오지 않아도 됨.

<br>

- 8개의 방향을 저장 후, 이동이 가능할 때만 이동시킴

![hamilton](/Users/yodayeong/Desktop/CS_STUDY/algorithms.assets/hamilton.jpeg)

- 마지막까지 탐색
  - (경로, 회로) if (k == n * m)
  - (회로) and s(start) in graph[v]

<br>

**기사의 여행 문제와 해밀턴 경로**

> **Description**
>
> n by m 체스보드에서 기사의 여행 문제를 해결하는 백트래킹 알고리즘을 구현하시오.
>
> Knight's Tour 문제는 해밀턴 경로(path)와 해밀턴 회로(circuit, cycle)를 찾는 문제로 구분할 수 있다.
>
> 해밀턴 회로는 출발 정점과 무관하게 회로의 수를 구할 수 있고,
>
> 해밀턴 경로는 출발 정점에 따라 가능한 경로의 수가 달라짐에 유의하시오.
>
> **Input**
>
> 첫 번째 줄에 체스보드의 크기 n(행의 크기)과 m(열의 크기)이 주어진다.
>
> 두 번째 줄에 출발정점의 개수 T가 주어진다.
>
> 이후로 T개의 출발정점이 i(row), j(col) 의 쌍으로 주어진다.
>
> **Output**
>
> 첫 번째 줄에 해밀턴 회로의 개수를 출력한다.
>
> 두 번째 줄부터 입력에서 주어진 출발정점 각각에 대해 해밀턴 경로의 수를 한 줄에 하나씩 출력한다.
>
> **Sample Input 1**
>
> ```
> 3 4
> 3
> 0 0
> 0 1
> 1 0
> ```
>
> **Sample Output 1**
>
> ```
> 0
> 2
> 0
> 4
> ```

```cpp
//기사의 여행 문제와 해밀턴 경로
//각 노드에서 이동할 수 있는 노드를 adjacency list로 만들어, 
//이동 가능 여부를 확인하고, 이동할 수 있으면 이동한다.

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m, s, cnt, cntc;
vector<vector<int>> graph;
vector<int> mark;

void make_graph() {
    //한 노드 당 8가지 방향으로 이동 가능
    int imov[] = {-2, -1, 1, 2, 2, 1, -1, -2};
    int jmov[] = {1, 2, 2, 1, -1, -2, -2, -1};

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            for(int k = 0; k < 8; k++) {
                int ni = i + imov[k];
                int nj = j + jmov[k];

                //adjacency list 생성
                if(ni >= 0 && nj >= 0 && ni < n && nj < m) {
                    graph[i * m + j].push_back(ni * m + nj);
                }
            }
        }
    }
}

void tour(int kth, int v) {
    //끝까지 투어를 마쳤다면,
    if(kth == n * m) {
        cnt++;
        
        vector<int> adj = graph[v];
        //회로 인지 체크
        if(find(adj.begin(), adj.end(), s) != adj.end()) {
            cntc++;
        }
        // cout << "solution #" << cnt << ":" << endl;

        // for(int i = 0; i < n; i++) {
        //     for(int j = 0; j < m; j++) {
        //         printf("%2d ", mark[i * m +j]);
        //     }
        //     cout << endl;
        // }
    }
    else {
        //현재 노드의 adjacency list를 돌면서
        for(int u: graph[v]) {
            //다음 노드가 방문 가능한지 체크
            if(mark[u] == 0) {
                mark[u] = kth + 1;
                tour(kth + 1, u);
                mark[u] = 0; //모든 정점을 돌아야 하기에 0으로 세팅
            }
        }
    }
}


int main() {
    cin >> n >> m;

    graph.resize(n * m, vector<int>(0));
    mark.resize(n * m, 0);

    make_graph();

    /*
    for(int v = 0; v < n * m; v++) {
        cout << v << ": ";
        for(int j = 0; j < graph[v].size(); j++) {
            cout << graph[v][j] << " ";
        }
        cout << endl;
    }
    */

   s = 1; //starting vertex
   mark[s] = 1; //mark starting vertex
   cntc = 0;
   tour(1, s);
   cout << cntc << endl; //해밀턴 회로의 개수

   int T;

   cin >> T;
    for(int i = 0; i < T; i++) {
        int a = 0, b = 0;
        
        cin >> a >> b;

        mark.resize(n * m, 0);
        fill(mark.begin(), mark.end(), 0);
        
        mark[(a * m) + b] = 1;
        cnt = 0;
        tour(1, (a * m) + b);
        cout << cnt << endl; //해밀턴 경로의 개수
    }
}
```

