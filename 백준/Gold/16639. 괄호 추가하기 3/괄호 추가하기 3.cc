#include<iostream>
#include<algorithm>
using namespace std;
int n;
char expr[20];
int num[10];
char op[10];
int dp_max[10][10];
int dp_min[10][10];

int calc(int a, int b, char o) {
    if (o == '+') return a + b;
    if (o == '-') return a - b;
    return a * b;
}

int main() {
    cin >> n >> expr;
    int m = n / 2 + 1; // 숫자 개수

    // 숫자와 연산자 분리
    for (int i = 0; i < m; i++) num[i] = expr[i * 2] - '0';
    for (int i = 0; i < m - 1; i++) op[i] = expr[i * 2 + 1];

    // 초기화
    for (int i = 0; i < m; i++) dp_max[i][i] = dp_min[i][i] = num[i];

    // 구간 DP
    for (int len = 1; len < m; len++) 
    {
        for (int i = 0; i + len < m; i++) 
        {
            int j = i + len;
            int maxv = -2147483647, minv = 2147483647;

            for (int k = i; k < j; k++) 
            {
                int a = calc(dp_max[i][k], dp_max[k + 1][j], op[k]);
                int b = calc(dp_max[i][k], dp_min[k + 1][j], op[k]);
                int c = calc(dp_min[i][k], dp_max[k + 1][j], op[k]);
                int d = calc(dp_min[i][k], dp_min[k + 1][j], op[k]);
                maxv = max({ maxv, a, b, c, d });
                minv = min({ minv, a, b, c, d });
            }
            dp_max[i][j] = maxv;
            dp_min[i][j] = minv;
        }
    }

    cout << dp_max[0][m - 1];
}