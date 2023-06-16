## Dynamic Programming - 0-1 배낭 문제와 동적계획법

물건을 선택하는 경우와 선택하지 않는 경우를 고려하여, 배낭에 넣을 수 있는 물건들의 가치 합의 최댓값을 구한다.

<br>

배낭의 용량을 넘지 않으면서, 가치가 최대가 되는 S의 부분집합 A 찾기

```
1. 재귀관계식 발견

*w는 아이템의 무게
*p는 아이템의 가치
*P[i][w]는 i번째에 w를 담았을 때의 optimal profit

P[i][w] = {
//현재 무게를 추가했을 때 배낭의 무게를 넘지 않는다면, 1. 배낭에 현재 무게를 더하지 않은 것과 2. 배낭에 현재 무게를 더한 것을 비교하여, 더 큰 값을 반환
maximum(P[i-1][w], pi + P[i-1][w-wi]), (if wi <= W) 
//현재 무게를 추가했을 때 배낭의 무게를 넘는다면, 이전까지의 무게를 더한 것만 반환
P[i-1][w], (if wi > W)
}

2. Bottom-up 방식(table, memoization)
```



**0-1 배낭문제와 동적계획법**

> **Description**
>
> 교재의 내용과 강의자료를 참고하여 0-1 배낭문제를 해결하는 알고리즘의 구현을 완성하시오.
>
> 강의자료에서 knapsack2() 또는 knapsack3()를 참조할 것.
>
> 단, 입력값은 단위 무게당 이익의 순서로 정렬되어 있지 않음에 유의하시오.
>
> 또한,알고리즘 실행 결과의 출력은 알고리즘의 실행과정에서결과 테이블 P에 저장한
>
> 무게(i) 또는 이익(j)이 0이 아닌 모든 항목 P[i][j]를 (i, j)의 오름차순으로 모두 출력한다는 것에 주의하시오.
>
> **Input**
>
> 첫 번째 줄에 아이템의 개수 n이 주어진다.
>
> 두 번째 줄에 n개의 무게 w[i]가 주어진다.
>
> 세 번째 줄에 n개의 이익 p[i]가 주어진다.
>
> 네 번째 줄에 배낭 무게의 개수 T가 주어진다.
>
> 이후로 T개의 줄에 한 줄에 하나씩 배낭 무게 W가 주어진다.
>
> **Output**
>
> 주어진 배낭 무게 W 각각에 대해 다음과 같이 출력한다.
>
> 첫 줄에 최대 이익 maxprofit을 출력한다.
>
> 이후로 알고리즘의 실행과정에서 결과 테이블 P에 저장한
>
> 무게(i) 또는 이익(j)이 0이 아닌모든 항목 P[i][j]를 (i, j)의 오름차순으로 모두 출력한다
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
> 200
> 1 10 50
> 1 20 50
> 1 30 50
> 2 20 140
> 2 30 190
> 3 30 200
> ```

````cpp
//0-1 배낭문제와 동적계획법

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

//물건 번호, 물건의 무게, 물건의 가치를 저장하는 구조체
typedef struct{
    int n;
    int W;
    int P;
} Ptable;

vector<Ptable> res; //선택한 물건들의 정보 저장

//물건의 번호와 무게를 기준으로 비교하여 오름차순 정렬
bool compare(Ptable a, Ptable b) {
    if(a.n < b.n) {
        return true;
    }
    else if(a.n > b.n) {
        return false;
    }
    else {
        if(a.W < b.W) {
            return true;
        }
        else {
            return false;
        }
    }
}

//물건의 무게와 가치를 비교하기 위한 함수
bool comparep(pair<int, int> a, pair<int, int> b) {
    return (a.second / a.first) > (b.second / b.first);
}

//최대 가치를 계산
//중복 계산을 피하기 위해 map 자료구조를 사용하여 계산 결과 저장
//pair<int, int>값을 key 값으로 가지고 int를 value 값으로 가짐
int knapsack3(int n, int W, vector<pair<int, int>> wp, map<pair<int, int>, int>& P) {
    if(n == 0 || W <= 0) {
        return 0;
    }
    
    int lvalue = (P.find(make_pair(n - 1, W)) != P.end()) ? P[make_pair(n - 1, W)] : knapsack3(n - 1, W, wp, P);
    int rvalue = (P.find(make_pair(n - 1, W - wp[n].first)) != P.end()) ? P[make_pair(n - 1, W - wp[n].first)] : knapsack3(n - 1, W - wp[n].first, wp, P);
    P[make_pair(n, W)] = (wp[n].first > W) ? lvalue : max(lvalue, wp[n].second + rvalue);

    Ptable table = {n, W, P[make_pair(n, W)]};
    //cout << n << " " << W << " " << P[make_pair(n,W) << "\n"]
    res.push_back(table);

    return P[make_pair(n, W)];
}

int main() {
    int n = 0, T = 0, W = 0;
    vector<int> w, p;
    vector<pair<int, int>> wp; //물건의 무게와 가치 저장

    cin >> n;

    w.resize(n + 1);
    p.resize(n + 1);
    wp.resize(n + 1);

    for(int i = 1; i <= n; i++) {
        cin >> w[i];
    }

    for(int i = 1; i <= n; i++) {
        cin >> p[i];
        wp[i] = make_pair(w[i], p[i]);
    }

    sort(wp.begin() + 1, wp.end(), comparep);

    cin >> T; //배낭의 개수
    for(int i = 0; i < T; i++) {
        map<pair<int, int>, int> P;
        res.clear();
        int maxprofit = 0;
        cin >> W; //배낭의 무게
        maxprofit = knapsack3(n, W, wp, P);

        cout << maxprofit << "\n";

        sort(res.begin(), res.end(), compare);

        for(int j = 0; j < res.size(); j++) {
            cout << res[j].n << " " << res[j].W << " " << res[j].P << "\n";
        }
    }
}
````