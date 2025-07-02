/*
행렬이 5개일 때
A(BCDE), (AB)(CDE), (ABC)(DE), (ABCD)E

행렬이 4개일 때
A(BCD), (AB)(CD), (ABC)D

행렬이 3개일 때
A(BC), (AB)C

행렬이 2개일 때
(AB)
*/

#pragma warning(disable:4996)  
#include <stdio.h>
#include <algorithm>
using namespace std;
int n, a[501], b[501], dp[501][501];
int main()
{
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
        scanf("%d%d", &a[i], &b[i]);


    for (int j = 2; j <= n; j++)
    {
        for (int i = 1; i <= n - (j - 1); i++) // dp[i번째 행렬부터][j번째 행렬까지]
        {
            int x = i, y = j + i - 1;
            dp[x][y] = 0x7fffffff;
            for (int k = x; k < y; k++) // dp[i][k], dp[k+1][j]
                dp[x][y] = min(dp[x][y], dp[x][k] + dp[k + 1][y] + a[x] * b[k] * b[y]);
        }

    }
    printf("%d", dp[1][n]);
    return 0;
}