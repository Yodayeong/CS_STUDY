//백준 18870 좌표 압축
//좌표 압축
//수의 범위가 매우 큰 상황에서,
//수의 값에 무관하게 좌표들 사이의 대소만 알면 될 때 사용

//1. 좌표 압축을 할 배열을 임시 배열에 중복이 없고 정렬된 상태로 둔다.
//*주로 std::sort, std::uniqe 함수 사용
//2. 압축할 배열의 각 수들이 임시 배열의 몇 번째 인덱스에 해당하는 수인지 찾는다.
//*주로 std::lower_bound 함수 사용

//ex)
//arr = [3, 4, 7, 1, 3, 4]
//tmp = [1, 3, 4, 7]
//좌표 압축 후 = [1, 2, 3, 0, 1, 2]

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> arr(n, 0);
    vector<int> tmp(n, 0);

    int temp;
    for(int i = 0; i < n; i++) {
        cin >> temp;
        arr[i] = temp;
        tmp[i] = temp;
    }

    sort(tmp.begin(), tmp.end());
    tmp.erase(unique(tmp.begin(), tmp.end()), tmp.end());

    for(int i = 0; i < n; i++) {
        int idx = lower_bound(tmp.begin(), tmp.end(), arr[i]) - tmp.begin(); //실제위치를 알고싶음
        cout << idx << " ";
    }
}