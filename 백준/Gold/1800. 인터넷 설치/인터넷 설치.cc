#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
constexpr int M = 1'000'000'007;
struct Node
{
    int node, ck, _max;
    Node(int a, int b, int c) : node(a), ck(b), _max(c) {}
};
int n, p, k, visit[1001][1001];
vector<pair<int, int>> graph[1001];
queue<Node> que;
void init()
{
    fastio;
    cin >> n >> p >> k;

    while (p--)
    {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].emplace_back(b, c);
        graph[b].emplace_back(a, c);
    }
}

int dijkstra(int limit)
{
    que = queue<Node>();
    for(int i = 0 ; i <= k ; ++i) for (int j = 1; j <= n; ++j) visit[i][j] = 0;

    que.emplace(1, 0, 0);
    visit[0][1] = 1;
    while (!que.empty())
    {
        auto [node, ck, _max] = que.front(); que.pop();
        for (const auto& [tnode, tcost] : graph[node])
        {
            if (!visit[ck][tnode] && max(_max, tcost) <= limit)
            {
                visit[ck][tnode] = 1;
                que.emplace(tnode, ck, max(_max, tcost));
                if (tnode == n) return max(_max, tcost);
            }
            if (ck + 1 <= k && tcost > limit && !visit[ck + 1][tnode])
            {
                visit[ck + 1][tnode] = 1;
                que.emplace(tnode, ck + 1, _max);
                if (tnode == n) return _max;
            }
        }

    }
    return -1;
}

void solution()
{
    int left = -1, right = M;

    while (left + 1 < right)
    {
        int mid = (left + right) >> 1;
        if (dijkstra(mid) >= 0) right = mid;
        else left = mid;
    }
    if (1'000'000'000 < left || right < 0) cout << -1;
    else cout << right;
}

int main()
{
    init();
    solution();
    return 0;
}
