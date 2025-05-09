#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;
int n, m, ex, dp[20][100000], depth[100000];
vector<int> graph[100000];
void dfs(int node, int d)
{
    depth[node] = d;
    for (const int& tnode : graph[node])
    {
        if (depth[tnode]) continue;
        dp[0][tnode] = node;
        dfs(tnode, d + 1);
    }
}
int main()
{
    scanf("%d", &n);
    for (int i = 1; i <= n; i *= 2) ex++;
    for (int i = 1; i < n; i++)
    {
        int a, b;
        scanf("%d%d", &a, &b); a--; b--;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    dfs(0, 1); // 각 노드의 깊이를 구함

    // 희소배열 생성
    for (int i = 1; i <= ex; i++)
        for (int j = 0; j < n; j++)
            dp[i][j] = dp[i - 1][dp[i - 1][j]];

    scanf("%d", &m);
    for(int i = 0 ; i < m ; i++)
    {
        int a, b, tmp;
        scanf("%d%d", &a, &b); a--; b--;
        if (depth[a] > depth[b])
        {
            tmp = a; a = b; b = tmp;
        }
        int diff = depth[b] - depth[a];

        for (int i = ex; i >= 0; i--)
        {
            if ((diff & (1 << i)) == 0) continue;
            b = dp[i][b];
        }
        while (a != b)
        {
            if (dp[0][a] == dp[0][b])
            {
                a = dp[0][a];
                break;
            }
            for (int i = 0; i <= ex; i++)
            {
                if (dp[i][a] == dp[i][b]) continue; // 조상의 조상의,, 로 뛰어넘을 수 있으니 같다면 continue
                a = dp[i][a];
                b = dp[i][b];
            }
        }
        printf("%d\n", a + 1);
    }
    return 0;
}
