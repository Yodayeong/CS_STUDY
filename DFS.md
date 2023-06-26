## DFS(Depth-First Search): 깊이 우선 탐색

그래프 전체를 탐색하는 방법 중 하나로, 넓게 탐색하는 것이 아니라 깊게 탐색하는 방법이다.

=> stack 또는 recursive로 구현할 수 있다.

<br>

- DFS의 특징
  - 정점 방문 시, 반드시 방문 여부(visited)를 검사하고, 방문 시 isVisited를 true로 표시한다.
  - 얻은 결과가 최단 경로라는 보장이 없다.

<br>

- 변수 설명

  1. int v, e
     - v는 정점의 개수, e는 정점 사이를 잇는 간선의 개수이다.

  2. vector<vector<int>> graph

     - 이중 vector를 사용함으로써 필요한 메모리만 할당해서 사용할 수 있다.

     - 정점의 개수를 먼저 입력 받은 후 .assign()함수를 이용해서 필요한 만큼 할당한다.

     - ``````c++
       //assign 함수를 통해서 vector<int>를 v+1개 할당
       graph.assign(v + 1, vector<int>(0, 0));
       ``````

     - 이후, 간선이 연결하는 두 정점을 입력 받으면서, 간선 정보를 graph에 입력한다.

     - ``````c++
       //인접 리스트를 사용하여 무방향 그래프를 표현
       int s, e;
       cin >> s >> e;
       graph[s].emplace_back(e);
       graph[e].emplace_back(s);
       ``````

  3. vector<bool> isVisited

     - 각 노드를 방문했는지 여부를 저장하는 변수이다.

     - vector로 선언한 이유는 정점의 개수를 입력 받아서 정점의 개수만큼만 메모리를 할당하기 위해서이다.

     - ``````c++
       //노드는 1번부터 v번까지이고, 아직 어떤 노드도 방문하지 않았기 때문에 false로 초기화
       isVisited.assign(v + 1, false);
       ``````

  <br>

  - DFS 진행 단계
    1. DFS를 시작할 노드를 정해서 매개변수로 전달한다.
    2. 전달 받은 매개변수가 현재 노드이므로, 현재 방문 중인 노드를 방문 처리 해준다.
    3. 현재 노드와 인접한 노드들을 반복문을 통해 하나씩 접근한다. 해당 노드를 다음 노드(next)로 설정한다.
    4. 다음 노드(next)를 이전에 방문했는지 확인한다. 
       - 만일 방문했다면, 다시 방문할 필요가 없으므로 지나간다. ( continue문 )
       - 아직 방문하지 않았다면, DFS를 재귀적으로 호출한다. ( DFS(next); )
    5. 2~4번을 더 이상 방문할 노드가 없을 때까지 반복한다.

  <br>

  - Code

    - ```c++
      //Parameters
      int v, e; //정점의 개수, 간선의 개수
      vector<vector<int>> graph; //인접 리스트
      vector<bool> isVisited; //정점 방문 여부 저장
      
      //Method
      void input() {
        cin >> v >> e;
        //메모리 공간 할당 및 초기화
        graph.assign(v + 1, vector<int> (0, 0));
        isVisited.assign(v + 1, false);
        
        for(int i = 0; i < e; i++) {
          int s, e;
          cin >> s >> e;
          //양방향 간선을 연결시킨다.
          graph[s].emplace_back(e);
          graph[e].emplace_back(s);
        }
      }
      
      void DFS(int cur) {
        isVisited[cur] = true;
        cout << "방문한 노드: " << cur << "\n";
        
        //현재 정점과 간선으로 연결되어 있는 모든 정점들을 둘러본다.
        for(int i = 0; i < graph[cur].size(); i++) {
          int next = graph[cur][i];
          //만일 방문하지 않았다면, 매개변수로 전달하여 DFS를 재귀적으로 호출한다.
          if(!isVisited[next]) {
            DFS(next);
          }
        }
      }
      ```