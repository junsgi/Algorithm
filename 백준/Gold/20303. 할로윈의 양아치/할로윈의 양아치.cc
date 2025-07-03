#pragma warning(disable:4996)  
#include <stdio.h>
#include <algorithm>
#include <vector>
#define M 30001
using namespace std;
int n, m, k, cost[M], cnt[M], p[M], dp[3001];
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
    for (auto& [w, v] : arr)
    {
        for (int j = k - 1; j >= 0; j--)
        {
            if (j - w >= 0)
                dp[j] = max(dp[j], dp[j - w] + v);
        }
    }
    printf("%d", dp[k - 1]);
    return 0;
}