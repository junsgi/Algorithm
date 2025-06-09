#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
#define M 1000000
using namespace std;
int n, m, r, ans, cost[100], graph[100][100];
int main()
{
    fill(&graph[0][0], &graph[0][0] + (100 * 100), M);
    scanf("%d%d%d", &n, &m, &r);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &cost[i]);
        graph[i][i] = 0;
    }
    for (int i = 0; i < r; i++)
    {
        int a, b, c;
        scanf("%d%d%d", &a, &b, &c); a--; b--;
        graph[a][b] = min(graph[a][b], c);
        graph[b][a] = min(graph[b][a], c);
    }
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
    for (int i = 0; i < n; i++)
    {
        int res = cost[i];
        for (int j = 0; j < n; j++)
        {
            if (i == j || graph[i][j] > m) continue;
            res += cost[j];
        }
        ans = max(ans, res);
    }
    printf("%d", ans);
    return 0;
}
