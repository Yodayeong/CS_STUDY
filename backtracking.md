## Backtracking

: 상태공간트리를 깊이 우선 탐색(DFS)로 탐색하는 알고리즘이다.

=> 방문 중인 노드에서 더 하위 노드로 가면 해답이 없는 경우, 해당 노드의 하위 트리를 방문하지 않고 부모 노드로 되돌아가는(backtrack) 알고리즘이다.

=> 임의의 집합에서 주어진 기준대로 원소의 순서를 선택하는 문제를 푸는데 적합하다.

<br>

- Pruning(가지치기)
  1. 백트래킹: 상태공간 트리를 dfs로 탐색하고
  2. 방문 중인 노드가 유망한지(promising) 체크
  3. 만약 유망하지 않다면, 부모 노드로 되돌아감

*이때, 상태 공간 트리를 실제로 구현할 필요는 없다. 현재 조사 중인 가지의 값에 대해서 추적만 하면 된다.

<br>

ex) 미로찾기

: 길을 찾아다니다가 벽을 맞닥뜨리면, 다시 왔던 길을 되돌아감

=> 일반적으로는 stack을 활용하지만, backtracking 문제에서는 트리 탐색 문제로 해결할 수 있다. dfs를 통해 트리 구조를 preorder로 방문할 수 있다.