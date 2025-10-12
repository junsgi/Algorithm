#include<iostream>
#include<queue>
#include<vector>
using namespace std;
int n, m, visit[501];
vector<int> graph[501];
queue<pair<int, int>> que;
int main()
{
    cin.tie(nullptr); cout.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cin >> n >> m;
    while(m--)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    int ans = 0;
    visit[1] = 1;
    que.push({1, 0});
    while(!que.empty())
    {
        auto [node, depth] = que.front(); que.pop();
        ++ans;
        for(int& tnode : graph[node])
        {
            if (visit[tnode]) continue;
            if (depth + 1 > 2) continue;
            visit[tnode] = 1;
            que.push({tnode, depth + 1});
        }
    }
    cout << ans - 1;
    return 0;
}