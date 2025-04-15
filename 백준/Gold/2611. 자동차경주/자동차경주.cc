#pragma warning(disable:4996)
#include<stdio.h>
#include<vector>
using namespace std;
int n, m, dp[1000], visit[1000];
vector<pair<int, int>> graph[1000];
int memo(int node, int depth)
{
    if (node == 0 && depth > 0)
        return 0;
    if (dp[node] != 0) return dp[node];
    for (pair<int, int>& t : graph[node])
    {
        int tnode = t.first, weight = t.second;
        if (visit[tnode]) continue;
        visit[tnode] = 1;
        dp[node] = max(dp[node], memo(tnode, depth + 1) + weight);
        visit[tnode] = 0;
    }
    return dp[node];
}
void print(int node)
{
    printf("%d ", node + 1);
    for (pair<int, int>& t : graph[node])
    {
        if (dp[node] != dp[t.first] + t.second) continue;
        print(t.first);
    }
}
int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; i++)
    {
        int a, b, c;
        scanf("%d%d%d", &a, &b, &c); a--;b--;
        graph[a].emplace_back(b, c);
    }
    printf("%d\n", memo(0, 0));
    print(0);
    printf("1");
    return 0;
}