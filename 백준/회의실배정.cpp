//백준 1931 회의실 배정
//끝나는 시간을 기준으로 오름차순 정렬 후,
//finish time <= start time을 만족하면
//배열에 추가

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    //정렬
    int start, end;
    vector<pair<int, int>> schedule;

    for(int i = 0; i < n; i++) {
        cin >> start >> end;
        schedule.push_back(make_pair(end, start));
    }

    sort(schedule.begin(), schedule.end());

    int cnt = 1;
    int time = schedule[0].first;
    for(int i = 1; i < n; i++) {
        if(schedule[i].second >= time) {
            cnt++;
            time = schedule[i].first;
        }
    }

    cout << cnt << endl;
    
}