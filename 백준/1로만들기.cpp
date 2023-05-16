// 백준 1463 1로 만들기
// dp..?
// 앞의 리스트를 탐색해서
// 만약 1이 있다면, 탐색을 멈추고
// 1이 없다면, 3가지 연산을 하고 뒤의 리스트에 추가한다.

#include <iostream>
#include <vector>
using namespace std;

int cnt = 0;
int start_index = 0;
int start_temp = 0;
int end_index = 1;
int end_temp = 1;
int x = 0;
vector<int> values(10000000, 0); //values의 size를 충분히 크게 안해줘서 계속 오류가 떳다 ㅜㅜ

int main() {
    int n;
    cin >> n;

    values[0] = n;

    while(x == 0) {
        //앞의 리스트에 1이 있는지 여부를 확인
        for(int i = start_index; i < end_index; i++) {
            if(values[i] == 1) {
                cout << cnt << endl;
                x = 1;
                break;
            }
        }
        //1이 없다면, 뒤의 리스트에 3가지 연산 결과를 추가해줌
        int now = 0;
        for(int i = start_index; i < end_index; i++) {
            now = values[i];
            values[end_temp++] = now - 1;
            if(!(now % 2)) {
                values[end_temp++] = now / 2;
            }
            if(!(now % 3)) {
                values[end_temp++] = now / 3;
            }
        }
        //수행이 끝나면, cnt를 증가해주고, 탐색범위(start_index, end_index) 갱신
        cnt += 1;
        start_index = end_index;
        end_index = end_temp;
    }

}