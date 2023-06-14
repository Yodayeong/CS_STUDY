## 분할 가능한 배낭문제

배낭문제에는 두가지 종류가 있다.

- 분할 가능한 배낭문제

  : 배낭에 물건을 담을 수 있는 만큼만 담는 행동이 가능하다.

- 0-1 배낭문제

  : 배낭에 물건을 담거나 담지 않는 두가지 행동만 할 수 있기 때문에 남아 있는 공간을 고려해야 한다.

<br>

분할 가능한 배낭문제는 greedy approach로 해결할 수 있다.

=> 물건을 단위 당 무게가 높은 것부터 내림차순으로 정렬하고, 순서대로 고르면 된다.

<br>

**분할가능한 배낭문제**

> **Description**
>
> 교재와 강의자료를 참고하여 분할가능한 배낭 문제를 해결하는 탐욕 알고리즘의 구현을 완성하시오.
>
> 입력은 아이템의 무게와 이익이 주어지고,
>
> 탐욕 알고리즘은 단위 무게당 이익이 가장 높은 순서대로 배낭에 담는 전략을 취한다.
>
> 입력으로 주어지는 값은 단위 무게당 이익으로 정렬되어 있지 않음에 주의하라.
>
> 단, 단위 무게당 이익이 같은 아이템은 없다고 가정해도 된다.
>
> **Input**
>
> 첫째 줄에 아이템의 개수 n이 주어진다.
>
> 둘째 줄에 n개의 아이템의 무게가 주어진다.
>
> 셋째 줄에 n개의 아이템별 이익이 주어진다.
>
> 넷째 줄에 도둑의 배낭 무게 W의 개수 T가 주어진다.
>
> 다섯째 줄부터 T개의 배낭 무게 W가 주어진다.
>
> **Output**
>
> 입력으로 주어진 각 W에 대해서
>
> 첫 줄에 탐욕법으로 배낭에 담을 수 있는 최대이익을 출력한다.
>
> 둘째 줄부터 배낭에 담은 아이템의 순서대로 무게와 이익의 쌍을 한 줄에 하나씩 출력한다.
>
> 다음 줄에는 다음에 주어지는 W에 대해서 위의 출력을 반복한다.
>
> **Sample Input 1**
>
> ```
> 3
> 5 10 20
> 50 60 140
> 1
> 30
> ```
>
> **Sample Output 1**
>
> ```
> 220
> 5 50
> 20 140
> 5 30
> ```

```cpp
//분할가능한 배낭문제
//greedy approach로, profit 순으로 정렬한다.

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef struct item* item_ptr;
typedef struct item{
    int id;
    int weight;
    int profit;
    int profit_per_unit; //=> profit / weight
} item_t;

int n, W;
vector<item_t> items;
vector<pair<int, int>> p; //배낭

bool compare_item(item_t i, item_t j) {
    if(i.profit_per_unit > j.profit_per_unit)
        return true;
    return false;
};

void knapsack(int& maxprofit, int& totweight) {
    maxprofit = totweight = 0;
    for(int i = 1; i <= n; i++) {
        //아이템의 무게가 배낭의 무게를 넘어서는지 체크
        if(totweight + items[i].weight <= W) {
            p.push_back(make_pair(items[i].weight, items[i].profit));
            maxprofit += items[i].profit;
            totweight += items[i].weight;
        }
        else {
            p.push_back(make_pair((W - totweight), (W - totweight) * items[i].profit_per_unit));
            maxprofit += (W - totweight) * items[i].profit_per_unit;
            totweight += (W - totweight);
            break;
        }
    }
}

int main() {
    cin >> n;

    items.resize(n + 1);
    for(int i = 1; i <= n; i++) {
        cin >> items[i].weight;
    }
    for(int i = 1; i <= n; i++) {
        cin >> items[i].profit;
        items[i].profit_per_unit = (int)(items[i].profit / items[i].weight);
    }

    sort(items.begin() + 1, items.end(), compare_item);

    int T = 0;
    cin >> T;

    for(int i = 0; i < T; i++) {
        int maxprofit = 0, totweight = 0;
        p.clear();
        cin >> W;
        
        knapsack(maxprofit, totweight);
        cout << maxprofit << "\n";
        int k = 0;
        for(k = 0; k < p.size(); k++) {
            if(p[k].first != 0) {
                cout << p[k].first << " " << p[k].second << "\n";
            }
        }
    }
}
```

