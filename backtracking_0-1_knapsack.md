## Backtracking - 0-1 배낭문제와 백트래킹

배낭의 용량을 넘지 않으면서 가치가 최대가 되는 S의 부분집합 A 찾기

<br>

``````
*n개의 아이템 집합: S
*아이템의 무게: w
*아이템의 가치: p
*배낭의 용량: W

백트래킹
- 상태공간 트리 구성
: 아이템을 담거나 담지 않거나 => 이진트리
- promising
: 1. 배낭에 아이템을 넣을 공간이 남아 있지 않으면, 유망하지 않다. (weight >= W)
  2. 현재까지 찾은 최적해의 이익이, 현재 노드에서 앞으로 얻을 수 있는 최대 이익보다 더 크면, 유망하지 않다. (bound <= maxprofit)
``````

<br>

**0-1 배낭문제와 백트래킹**

> **Description**
>
> 교재와 강의자료를 참고하여 0-1 배낭문제를 해결하는 Algorithm 5.7을 완성하시오.
>
> 단, 문제의 입력은 단위무게당 이익순으로 정렬되어 있지 않음에 유의하시오.
>
> 또한, 알고리즘의 출력은 알고리즘의 실행 단계별로
>
> 상태공간트리의 각 노드에서의 상태를 출력해야 함에 주의하시오.
>
> **Input**
>
> 첫번째 줄에 아이템의 개수 n과 배낭의 무게 W가 주어진다.
>
> 두번째 줄에 n개의 아이템 무게 w[i]가 주어진다.
>
> 세번째 줄에 n개의 아이템 이익 p[i]가 주어진다.
>
> **Output**
>
> 첫 번째 줄부터 한 줄에 하나씩 상태공간트리를 방문하는 노드의 상태를 출력하시오.
>
> 노드 상태는 다음과 같은 순서로 출력한다.
>
> i weight profit bound maxprofit
>
> 상태를 출력하는 순서는 Algorithm 5.7의 노드 실행 순서이다. (즉, DFS with Pruning의 노드 순회 순서임)
>
> 노드의 상태 출력이 끝나는 다음 줄에 최대이익을 출력한다.
>
> 이후로 배낭에 담은 아이템을 한 줄에 하나씩 무게와 이익 순서로 출력한다.
>
> 아이템을 출력하는 순서는 처음에 단위무게당 이익으로 정렬한 순서대로 출력함에 주의할 것.
>
> **Sample Input 1**
>
> ```
> 4 16
> 2 5 10 5
> 40 30 50 10
> ```
>
> **Sample Output 1**
>
> ```
> 0 0 0 115 0
> 1 2 40 115 40
> 2 7 70 115 70
> 3 17 120 115 70
> 3 7 70 80 70
> 4 12 80 80 80
> 4 7 70 70 80
> 2 2 40 98 80
> 3 12 90 98 90
> 4 17 100 98 90
> 4 12 90 90 90
> 3 2 40 50 90
> 1 0 0 82 90
> 90
> 2 40
> 10 50
> ```

```cpp
//0-1 배낭문제와 백트래킹
//상태 공간 트리를 구성하고, promising 한지 체크해준다.

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef struct{
    int w;
    int p;
    int pnw;
}ptable;

vector<ptable> pt;

vector<int> w, p, include, bestset;
int n, W, maxprofit;
int bound1;

bool compare(ptable a, ptable b) {
    return a.pnw > b.pnw;
}

//유망한지 판단
bool promising(int i, int profit, int weight) {
    int j, k, totweight;
    float bound;

    //1. 배낭에 아이템을 넣을 공간이 남아 있지 않다. => non-promising
    if(weight >= W) {
        cout << i << " " << weight << " " << profit << " " << bound1 << " " << maxprofit << "\n";
        return false;
    }
    //2. 현재까지 찾은 최적해의 이익이, 현재 노드에서 앞으로 얻을 수 있는 최대 이익보다 더 크다. => non-promising
    else {
        j = i + 1;
        bound = profit;
        totweight = weight;
        while(j <= n && totweight + w[j] <= W) {
            totweight += w[j];
            bound += p[j];
            j++;
        }
        k = j;
        if(k <= n) {
            bound += (W - totweight) * ((float)p[k] / w[k]);
        }
        bound1 = bound;
        cout << i << " " << weight << " " << profit << " " << bound1 << " " << maxprofit << "\n";
        return bound > maxprofit;
    }
}

void array_copy(vector<int> a, vector<int>& b) {
    b.clear();
    for(int i = 0; i < a.size(); i++) {
        b.push_back(a[i]);
    }
}

void knapsack4(int i, int profit, int weight) {
    if(weight <= W && profit > maxprofit) {
        maxprofit = profit;
        array_copy(include, bestset);
    }
    if(promising(i, profit, weight)) {
        //left-tree: 다음 아이템을 포함하는 경우
        include[i + 1] = true;
        knapsack4(i + 1, profit + p[i + 1], weight + w[i + 1]);
        //right-tree: 다음 아이템을 포함하지 않는 경우
        include[i + 1] = false;
        knapsack4(i + 1, profit, weight);
    }
}

int main() {
    cin >> n >> W;

    w.resize(n + 1);
    p.resize(n + 1);
    include.resize(n + 1);

    pt.resize(n + 1);

    for(int i = 1; i <= n; i++) {
        cin >> pt[i].w;
    }
    for(int i = 1; i <= n; i++) {
        cin >> pt[i].p;
        pt[i].pnw = pt[i].p / pt[i].w;
    }

    //먼저 단위 무게당 이익 순으로 정렬
    sort(pt.begin() + 1, pt.end(), compare);

    for(int i = 1; i <= n; i++) {
        w[i] = pt[i].w;
        p[i] = pt[i].p;
    }

    maxprofit = 0;

    knapsack4(0, 0, 0);

    cout << maxprofit << endl;

    for(int i = 1; i <= n; i++) {
        if(bestset[i]) {
            cout << w[i] << " " << p[i] << "\n";
        }
    }
}
```

