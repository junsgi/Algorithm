#pragma warning(disable:4996)  
#include <stdio.h>
#include <algorithm>
#define M 2511
using namespace std;
int len, dp[M][M], ans[M];
char n[M];
int p(int x, int y)
{
    if (x >= y) return 1;
    if (n[x] != n[y]) return 0;
    return p(x + 1, y - 1);
}
void print()
{
    for (int i = -1; i < len; i++)
    {
        for (int j = -1; j < len; j++)
        {
            if (i == -1)
                printf("%3d", j);
            else if (j == -1)
                printf("%3d", i);
            else
                printf("%3d", dp[i][j]);
        }
        printf("\n");
    }
}
int main()
{
    scanf("%s", n + 1);
    for (len = 1; n[len]; len++);
    for (int term = 0; term < len; term++)
        for (int idx = 1; idx < len - term; idx++)
            if (p(idx, idx + term))
                dp[idx][idx + term] = 1;
    for (int end = 1; end < len; end++)
    {
        ans[end] = 3000;
        for (int st = 1; st <= end; st++)
        {
            if (dp[st][end])
                ans[end] = min(ans[end], ans[st - 1] + 1);
        }
    }
    printf("%d", ans[len - 1]);
    return 0;
}