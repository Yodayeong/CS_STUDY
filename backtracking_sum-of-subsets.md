## Backtracking - 부분집합의 합 문제

원소가 n개인 양의 정수 집합 w와, 양의 정수 W가 주어졌을 때, 합이 W가 되는 부분 집합을 모두 찾아라.

=> 백트래킹(상태 공간 트리를 만들어 풀자!)

<br>

pruning 전략

``````
검색하기 전에, 정수 원소를 오름차순으로 정렬

- weight: 레벨 i까지 모든 정수 원소의 합
weight + w(i+1) > W : 유망하지 않다.

- total: 남은 정수 원소의 합
weight + total < W : 유망하지 않다.
``````

<br>

**부분집합의 합 문제**

> **Description**
>
> 교재와 강의자료를 참고하여 Sum-of-Subsets 문제를 푸는 Algorithm 5.4의 구현을 완성하시오.
>
> n개의 원소를 가진 정수의 집합 S가 주어지고,
>
> 임의의 정수 W가 주어졌을 때,
>
> 합이 W가 되는 부분집합의 개수와 각 부분집합을 출력하도록 하시오.
>
> **Input**
>
> 첫 줄에 원소의 개수 n과 임의의 정수 W가 주어진다.
>
> 둘째 줄에 n개의 정수가 주어진다.
>
> **Output**
>
> 첫 줄에 원소의 합이 W가 되는 부분집합의 개수를 출력한다.
>
> 둘째 줄부터 원소의 합이 W가 되는 모든 부분집합을 한 줄에 하나씩 출력한다.
>
> 단, 부분집합에서의 원소 출력 순서는 주어진 S의 원소 순서와 동일해야 한다. (백트래킹 순서대로)
>
> **Sample Input 1**
>
> ```
> 4 13
> 3 4 5 6
> ```
>
> **Sample Output 1**
>
> ```
> 1
> 3 4 6
> ```
>
> **Sample Input 2**
>
> ```
> 3 10
> 1 2 3
> ```
>
> **Sample Output 2**
>
> ```
> 0
> ```

```cpp
//부분집합의 합 구하기
//상태공간 트리를 만들어서, 조건에 맞지 않으면 pruning 하자!

#include <iostream>
#include <vector>
using namespace std;

vector<int> include, w;
vector<vector<int>> res;
int cnt;
int W;

//1. 지금껏 더한 subset의 무게와 남은 total을 더했을 때, W를 넘길 수 있어야 promising하다.
//2. 지금껏 더한 subset의 무게가 W인 경우, 지금껏 더한 subset의 무게와 지금 더하려는 무게가 W 이하여야 promising하다.
bool promising(int i, int weight, int total) {
    return (weight + total >= W) && (weight == W || weight + w[i + 1] <= W);
}

void sum_of_subsets(int i, int weight, int total) {
    if(promising(i, weight, total)) {
        //유망한데, 지금껏 더한 subset의 무게가 W에 도달했다면,
        if(weight == W) {
            vector<int> a;
            for(int j = 1; j <= i; j++) {
                if(include[j]) {
                    a.push_back(w[j]);
                }
            }
            //a의 size가 0이 아니라면, cnt를 증가하고,
            if(a.size()) {
                cnt++;
            }
            //res에 a를 넣어준다.
            res.push_back(a);
        }
        //유망은 하지만, 지금껏 더한 subset의 무게가 W에 도달하지 못했다면,
        else {
            //왼쪽 subtree
            include[i + 1] = true;
            sum_of_subsets(i + 1, weight + w[i + 1], total - w[i + 1]);
            //오른쪽 subtree
            include[i + 1] = false;
            sum_of_subsets(i + 1, weight, total - w[i + 1]);
        }
    }
}

int main() {
    int n = 0, total = 0;

    cin >> n >> W;

    include.resize(n + 1);
    w.resize(n + 1);

    for(int i = 1; i <= n; i++) {
        cin >> w[i];
        total += w[i];
    }
    
    if(total < W) {
        cout << "0";
        return 0;
    }

    sum_of_subsets(0, 0, total);

    cout << cnt << "\n";
    for(int i = 0; i < res.size(); i++) {
        int j = 0;
        for(j = 0; j < res[i].size() - 1; j++) {
            cout << res[i][j] << " ";
        }
        cout << res[i][j] << endl;
    }
}
```

