#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
using namespace std;
long long n, ans, dp[101][10][1 << 10], m = 1000000000;
int main()
{
    // 자릿수, 가장 앞에 위치한 수, 비트 연산을 통해 0부터 9의 존재

    // 초기화
    // 한 자릿수이면서 i로 시작하고 i를 포함하는 경우 추가
    for (int i = 1; i < 10; i++) dp[1][i][1 << i] = 1;

    // dp
    for (int i = 2; i <= 100; i++) // 자릿수
    {
        for (int j = 0; j < 10; j++) // 앞자리
        {
            for (int k = 1; k < (1 << 10); k++) // 0b0000000001 ~ 0b1111111111 경우의 수 모두 탐색
            {
                // k에 현자 앞자리수 j를 포함한 위치
                if (j != 0) dp[i][j][k | (1 << j)] += dp[i - 1][j - 1][k];
                if (j != 9) dp[i][j][k | (1 << j)] += dp[i - 1][j + 1][k];
                dp[i][j][k | (1 << j)] %= m;
            }
        }
    }
    scanf("%lld", &n);

    // n자릿수, i로 시작, (1 << 10) - 1 == 1023 == 0b1111111111
    for (int i = 0; i < 10; i++)
        ans = (ans + dp[n][i][(1 << 10) - 1]) % m; 
    printf("%lld", ans);
    return 0;
}
