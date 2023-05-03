//백준 1992 쿼드트리
//분할정복 문제

#include <iostream>
using namespace std;

int n;
string s;
int scene[100][100];

void solve(int x, int y, int size) {
    for(int i = x; i < x + size; i++) {
        for(int j = y; j < y + size; j++) {
            if(scene[i][j] != scene[x][y]) {
                cout << "(";
                solve(x, y, size / 2);
                solve(x, y + size / 2, size / 2);
                solve(x + size / 2, y, size / 2);
                solve(x + size / 2, y + size / 2, size / 2);
                cout << ")";
                return;
            }
        }
    }
    cout << scene[x][y];
}

int main() {
    cin >> n;

    for(int i = 0; i < n; i++) {
        cin >> s;
        for(int j = 0; j < n; j++) {
            scene[i][j] = s[j] - '0';
        }
    }

    solve(0, 0, n);
}