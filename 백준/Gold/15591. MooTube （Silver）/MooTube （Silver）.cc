#include<iostream>
#include<queue>
#include<vector>
using namespace std;
int n, q, visit[5001], cnt;
vector<pair<int, int>> graph[5001];
queue<int> que;
void input()
{
    cin.tie(nullptr); cout.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cin >> n >> q;
    for (int i = 1; i < n; ++i)
    {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].emplace_back(b, c);
        graph[b].emplace_back(a, c);
    }
}
int bfs(int k, int v)
{
    int res = -1;
    que.push(v);
    visit[v] = ++cnt;
    while (!que.empty())
    {
        int node = que.front(); que.pop();
        ++res;
        for (auto& [tnode, cost] : graph[node])
        {
            if (k > cost) continue;
            if (visit[tnode] == cnt) continue;
            visit[tnode] = cnt;
            que.push(tnode);
        }
    }
    return res;
}
void solution()
{
    while (q--)
    {
        int k, v;
        cin >> k >> v;
        cout << bfs(k, v) << '\n';
    }
}
int main()
{
    input();
    solution();
    return 0;
}