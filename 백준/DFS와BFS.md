## [백준/1260] DFS와 BFS

> ## 문제
>
> 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
>
> ## 입력
>
> 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
>
> ## 출력
>
> 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
>
> ## 예제 입력 1
>
> ```
> 4 5 1
> 1 2
> 1 3
> 1 4
> 2 4
> 3 4
> ```
>
> ## 예제 출력 1
>
> ```
> 1 2 4 3
> 1 2 3 4
> ```

<br>

**dfs와 bfs**

- DFS(Depth First Search)
  - 시작점부터, 다음 branch로 넘어가기 전까지, 해당 branch를 완벽하게 탐색하고 넘어가는 방법
  - 재귀함수나 스택으로 구현
  - 노드 방문 시, visited 여부를 반드시 검사해야 한다.
- BFS(Breadth First Search)
  - 시작 노드에서 가장 가까운 노드부터 우선적으로 탐색하는 알고리즘
  - 큐를 이용하여 구현
  - 특정 조건의 최단 경로 알고리즘을 계산할 때 사용

<br>

**dfs 연습**

```cpp
#include <iostream>
#include <vector>

using namespace std;

bool visited[9];
vector<int> graph[9];

//재귀함수를 통한 구현
void dfs(int v) {
    visited[v] = true;
    cout << v << " ";
    for(int i = 0; i < graph[v].size(); i++) {
        if(!visited[graph[v][i]]) {
            dfs(graph[v][i]);
        }
    }
}

int main() {
    graph[1].push_back(2);
    graph[1].push_back(3);
    graph[1].push_back(8);

    graph[2].push_back(1);
    graph[2].push_back(7);

    graph[3].push_back(1);
    graph[3].push_back(4);
    graph[3].push_back(5);

    graph[4].push_back(3);
    graph[4].push_back(5);

    graph[5].push_back(3);
    graph[5].push_back(4);

    graph[6].push_back(7);

    graph[7].push_back(2);
    graph[7].push_back(6);
    graph[7].push_back(8);

    graph[8].push_back(1);
    graph[8].push_back(7);
    
    dfs(1);
}
```

<br>

**bfs 연습**

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼낸 뒤, 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입 후 방문 처리
3. 2번 반복

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

bool visited[9];
vector<int> graph[9];

void bfs(int v) {
    queue<int> q;
    q.push(v);
    visited[v] = true;
    
    while(!q.empty()) {
        int x = q.front();
        q.pop();
        cout << x << " ";
        for(int i = 0; i < graph[x].size(); i++) {
            if(!visited[graph[x][i]]) {
                q.push(graph[x][i]);
                visited[graph[x][i]] = true;
            }
        }
    }
}

int main() {
    graph[1].push_back(2);
    graph[1].push_back(3);
    graph[1].push_back(8);

    graph[2].push_back(1);
    graph[2].push_back(7);

    graph[3].push_back(1);
    graph[3].push_back(4);
    graph[3].push_back(5);

    graph[4].push_back(3);
    graph[4].push_back(5);

    graph[5].push_back(3);
    graph[5].push_back(4);

    graph[6].push_back(7);

    graph[7].push_back(2);
    graph[7].push_back(6);
    graph[7].push_back(8);

    graph[8].push_back(1);
    graph[8].push_back(7);

    bfs(1);
}

```

<br>

**문제 풀이**

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

#define INF 100001

int N, M, V;
bool visited[INF];
vector<int> graph[INF];

void dfs(int v) {
    visited[v] = true;
    cout << v << " ";
    int size = (int)graph[v].size();
    for(int i = 0; i < size; i++) {
        if(!visited[graph[v][i]]) {
            dfs(graph[v][i]);
        }
    }
}

void bfs(int v) {
    queue<int> q;
    q.push(v);
    visited[v] = true;
    
    while(!q.empty()) {
        int x = q.front();
        q.pop();
        cout << x << " ";
        int size = (int)graph[x].size();
        for(int i = 0; i < graph[x].size(); i++) {
            if(!visited[graph[x][i]]) {
                q.push(graph[x][i]);
                visited[graph[x][i]] = true;
            }
        }
    }
}

int main() {
    cin >> N >> M >> V;
    
    int u, v;
    for(int i = 0; i < M; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
        sort(graph[u].begin(), graph[u].end());
        sort(graph[v].begin(), graph[v].end());
    }
    
    dfs(V);
    cout << endl;
    
    for(int i = 1; i <= N; i++) {
        visited[i] = false;
    }
    
    bfs(V);
}
```

