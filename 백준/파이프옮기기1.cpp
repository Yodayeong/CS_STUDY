//백준 17070 파이프 옮기기 1
//dp(dynamic programming)
//이제껏 계산한 값들을 배열에 저장하여 불필요한 연산을 줄이는 알고리즘

#include <iostream>
using namespace std;

int main() {
    //n과 집상태 입력받기
    int n;
    cin >> n;

    int layer[n][n];
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> layer[i][j];
        }
    }

    //해당 배열에 파이프가 가로로 놓여있는지, 세로로 놓여있는지, 대각선으로 놓여있는지 체크
    //dp[][][0] => 가로
    //dp[][][1] => 세로
    //dp[][][2] => 대각선

    //dp 0으로 초기화
    int dp[n][n][3];
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            for(int k = 0; k < 3; k++) {
                dp[i][j][k] = 0;
            }
        }
    }
 
    //(0, 1)에 파이프가 가로로 놓여있는 것으로 시작
    dp[0][1][0] = 1;
    dp[0][1][1] = 0;
    dp[0][1][2] = 0;
    
    //놓여진 파이프가 가로인지, 세로인지, 대각선인지 먼저 체크 후,
    //다음 파이프를 놓아야 하는 위치의 집 상태가 0이면,
    //다음 파이프의 값을 이전까지 오는 경우의 수를 더한 값으로 갱신해준다.
    for(int i = 0; i < n; i++) {
        for(int j = 1; j < n; j++) {
            if(dp[i][j][0] >= 1) {
                if(layer[i][j+1] == 0) {
                    dp[i][j+1][0] += dp[i][j][0];
                }
                if(layer[i][j+1] == 0 && layer[i+1][j] == 0 && layer[i+1][j+1] == 0) {
                    dp[i+1][j+1][2] += dp[i][j][0];
                }
            }
            if(dp[i][j][1] >= 1) {
                if(layer[i+1][j] == 0) {
                    dp[i+1][j][1] += dp[i][j][1];
                }
                if(layer[i][j+1] == 0 && layer[i+1][j] == 0 && layer[i+1][j+1] == 0) {
                    dp[i+1][j+1][2] += dp[i][j][1];
                }
            }
            if(dp[i][j][2] >= 1) {
                if(layer[i][j+1] == 0) {
                    dp[i][j+1][0] += dp[i][j][2];
                }
                if(layer[i+1][j] == 0) {
                    dp[i+1][j][1] += dp[i][j][2];
                }
                if(layer[i][j+1] == 0 && layer[i+1][j] == 0 && layer[i+1][j+1] == 0) {
                    dp[i+1][j+1][2] += dp[i][j][2];
                }
            }
        }
    }

    //마지막 칸의 가로, 세로, 대각선 파이프의 수를 더한 값을 출력
    cout << dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2] << endl;
    
}