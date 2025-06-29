#pragma warning(disable:4996)  
#include <stdio.h>
#include <algorithm>
using namespace std;
int n, len, x, y, ans, arr[100000], dp[100000][5][5];
int graph[5][5] = { 1, 2, 2, 2, 2, 0, 1, 3, 4, 3, 0, 3, 1, 3, 4, 0, 4, 3, 1, 3, 0, 3, 4, 3, 1 };
int memo(int a, int b, int depth)
{
    if (depth == len - 1) return 0;
    if (a && b && a == b) return 999999999;
    if (dp[depth][a][b] != -1) return dp[depth][a][b];
    dp[depth][a][b] = min(memo(a, arr[depth], depth + 1) + graph[b][arr[depth]], memo(arr[depth], b, depth + 1) + graph[a][arr[depth]]);
    return dp[depth][a][b];
}
int main()
{
    fill(&dp[0][0][0], &dp[0][0][0] + (100000 * 5 * 5), -1);
    while (1)
    {
        scanf("%d", &arr[len++]);
        if (arr[len - 1] == 0) break;
    }
    printf("%d", memo(0, 0, 0));
    return 0;
}