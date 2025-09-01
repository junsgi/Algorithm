#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int n, visit[10'001], cost[10'001], dp[2][10'001], ck;
vector<int> tree[10'001], path;
void dfs(int node)
{
    visit[node] = 1;
    dp[0][node] = cost[node];
    for (int& tnode : tree[node])
    {
        if (visit[tnode]) continue;
        dfs(tnode);
        dp[0][node] += dp[1][tnode];
        dp[1][node] += max(dp[0][tnode], dp[1][tnode]);
    }
}
void p(int node, int prev)
{
    if (dp[0][node] > dp[1][node] && visit[prev] != 2)
    {
        visit[node] = 2;
        path.push_back(node);
    }
    for (int& tnode : tree[node])
    {
        if (tnode == prev) continue;
        p(tnode, node);
    }
}
int main()
{
    cin.tie(nullptr); cout.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cin >> n;
    for (int i = 1; i <= n; ++i)
        cin >> cost[i];
    for (int i = 0; i < n - 1; ++i)
    {
        int a, b;
        cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }
    dfs(1);
    p(1, 1);
    sort(path.begin(), path.end());
    cout << max(dp[0][1], dp[1][1]);
    cout << '\n';
    for (int& i : path)
        cout << i << ' ';
    return 0;
}