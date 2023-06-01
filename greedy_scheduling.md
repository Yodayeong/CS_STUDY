## Greedy - 스케쥴링

- 스케쥴링: total time(작업을 기다리고, 수행하는 시간)을 minimize 하는 것이 목표

<br>

**deadline이 있는 스케쥴링**

- 각 작업은 동일한 complete time을 가짐

- 데드라인 안에 끝내는 작업은 profit을 얻음

- 데드라인 이후에 스케쥴링 된다면, profit을 얻지 못함

- => 목표: profit의 총합을 극대화

- ex)

  ![scheduling1](/Users/yodayeong/Desktop/CS_STUDY/algorithms.assets/scheduling1.jpeg)

  ![scheduling2](/Users/yodayeong/Desktop/CS_STUDY/algorithms.assets/scheduling2.jpeg)

<br>

**greedy approach**

- 보상을 내림차순으로 정렬
- 작업을 추가했을 때, 작업이 적절하다면 스케줄에 작업 추가
- 추가할 작업이 없을 때까지 반복

<br>

**데드라인 스케줄링 문제**

> **Description**
>
> 교재와 강의자료를 참고하여 Algorithm 4.4 Scheduling with Deadlines 의 구현을 완성하시오.
>
> 입력값은 profit의 내림차순으로 이미 정렬이 되어 있다고 가정해도 된다.
>
> 출력은 최대 이익과 함께 feasible sequence의 profit을 순서대로 출력한다.
>
> **Input**
>
> 첫째 줄에 job의 개수 n이 주어진다.
>
> 둘째 줄에 n개의 deadline이 주어진다.
>
> 셋째 줄에 n개의 profit이 주어진다.
>
> 단, profit은 내림차순으로 정렬되어 있다.
>
> **Output**
>
> 첫 줄에 최대 이익의 값을 출력한다.
>
> 둘째 줄에 Algorithm 4.4가 발견한 job sequence의 순서대로 각 job의 profit을 출력한다.
>
> **Sample Input 1**
>
> ```
> 7
> 3 1 1 3 1 3 2
> 40 35 30 25 20 15 10
> ```
>
> **Sample Output 1**
>
> ```
> 100
> 35 40 25
> ```

```c++
//데드라인 스케줄링 문제
//profit 순으로의 정렬은 이미 되어있기 때문에,
//값을 추가했을 때, deadline에 알맞게 정렬 되어 있는지만 확인하면 된다.

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<int> matrix_t;

bool is_feasible(matrix_t& deadline, matrix_t& temp) {
    for(int i = 1; i < temp.size(); i++) {
        if(i > deadline[temp[i]])
            return false;
    }
    return true;
}

void scheduling(int n, matrix_t& deadline, matrix_t& schedule_vec) {
    matrix_t temp;

    schedule_vec.clear();
    schedule_vec.push_back(0);
    schedule_vec.push_back(1);
    for(int i = 2; i <= n; i++) {
        temp.resize(schedule_vec.size());
        copy(schedule_vec.begin(), schedule_vec.end(), temp.begin());

        //적절한 위치에 새로운 값 insert
        int j = 1;
        while(j < temp.size() && deadline[i] >= deadline[temp[j]]) {
            j++;
        }
        temp.insert(temp.begin() + j, i);
        
        //값이 feasible 한 경우에만 집합 새로 갱신
        if(is_feasible(deadline, temp)) {
            schedule_vec.resize(temp.size());
            copy(temp.begin(), temp.end(), schedule_vec.begin());
        }
    }
}

int main() {
    int n;
    cin >> n;

    matrix_t deadline(n+1, 0);
    matrix_t profit(n+1, 0);
    matrix_t schedule_vec(n+1, 0);

    for(int i = 1; i <= n; i++) {
        cin >> deadline[i];
    }
    for(int i = 1; i <= n; i++) {
        cin >> profit[i];
    }

    scheduling(n, deadline, schedule_vec);

    int result = 0;
    for(int i = 1; i < schedule_vec.size(); i++) {
        result += profit[schedule_vec[i]];
    }
    cout << result << endl;

    for(int i = 1; i < schedule_vec.size(); i++) {
        if(i == schedule_vec.size() - 1)
            cout << profit[schedule_vec[i]] << endl;
        else
            cout << profit[schedule_vec[i]] << " ";
    }
}
```

