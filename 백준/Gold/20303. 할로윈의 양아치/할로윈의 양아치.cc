#pragma warning(disable:4996)  
#include <stdio.h>
#include <algorithm>
#include <vector>
#define M 30001
using namespace std;
int n, m, k, cost[M], cnt[M], p[M], dp[M][3001];
vector<pair<int, int>> arr;
int find(int node) { return node == p[node] ? (node) : (p[node] = find(p[node])); }
void Union(int x, int y)
{
    int fx = find(x), fy = find(y);
    if (fx == fy) return;
    if (fx > fy) swap(fx, fy);
    p[fy] = fx;
    cost[fx] += cost[fy];
    cnt[fx] += cnt[fy];
}
int main()
{
    scanf("%d%d%d", &n, &m, &k);
    for (int i = 1; i <= n; i++)
    {
        scanf("%d", &cost[i]);
        p[i] = i;
        cnt[i] = 1;
    }
    for (int i = 0; i < m; i++)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        Union(a, b);
    }
    for (int i = 1; i <= n; i++)
    {
        if (p[i] != i) continue;
        arr.emplace_back(cnt[i], cost[i]);
    }
    for (int i = 1 ; i <= arr.size() ; i++)
    {
        for (int j = 1; j < k; j++)
        {
            dp[i][j] = dp[i - 1][j];
            if (j - arr[i - 1].first >= 0)
                dp[i][j] = max(dp[i][j], dp[i - 1][j - arr[i - 1].first] + arr[i - 1].second);
        }
    }
    printf("%d", dp[arr.size()][k - 1]);
    return 0;
}