// 백준 20440 🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵 - 1

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
int start, finish;
vector<int> times(2100000001, 0); //start값을 담음

int main() {
    cin >> n;

    for(int i = 0; i < n; i++) {
        cin >> start >> finish;
        for(int j = start; j < finish; j++) {
            times[j] += 1;
        }
    }
    
    auto max_element = std::max_element(times.begin(), times.end());

    int result_start, result_end;
    for(int i = 0; i < 2100000001; i++) {
        if(times[i] == *max_element) {
            result_start = i;
            break;
        }
    }
    for(int i = start; i < 2100000001; i++) {
        if(times[i] != *max_element) {
            result_end = i;
            break;
        }
    }

    cout << *max_element << endl;
    cout << result_start << " " << result_end << endl;
    
}