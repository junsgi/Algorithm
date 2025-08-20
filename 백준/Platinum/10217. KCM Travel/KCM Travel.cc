#pragma warning(disable:4996)
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
struct Node
{
    int node, cost, time;
    Node(int a, int b, int c) : node{ a }, cost{ b }, time{ c } {}
    bool operator>(const Node& other) const {
        return time > other.time;
    }
};
constexpr int MAX = 1 << 25;
int n, m, k, cost[10'001][101];
vector<Node> graph[101];
priority_queue<Node, vector<Node>, greater<Node>> heap;
void init()
{
    scanf("%d%d%d", &n, &m, &k);
    for (int i = 0; i <= n; i++)
    {
        graph[i].clear();
        for (int j = 0; j <= m; j++)
            cost[j][i] = MAX;
    }
    for (int i = 0; i < k; i++)
    {
        int a, b, c, d;
        scanf("%d%d%d%d", &a, &b, &c, &d);
        graph[a].emplace_back(b, c, d);
    }
    for (int i = 1; i <= n; i++)
    {
        sort(graph[i].begin(), graph[i].end(), [&](const Node& x, const Node& y) { return x.time < y.time; });
    }
}
void solution()
{
    heap.emplace(1, 0, 0);
    cost[0][1] = 0;
    while (!heap.empty())
    {
        auto [node, _cost, time] = heap.top();
        heap.pop();
        if (node == n) break;
        if (cost[_cost][node] < time) continue;

        for (const auto& [tnode, tcost, tTime] : graph[node])
        {
            if (tcost + _cost > m) continue;
            if (cost[tcost + _cost][tnode] <= time + tTime) continue;
            for (int i = _cost + tcost + 1; i <= m; i++)
            {
                if (cost[i][tnode] <= time + tTime) break;
                cost[i][tnode] = time + tTime;
            }
            cost[tcost + _cost][tnode] = time + tTime;
            heap.emplace(tnode, tcost + _cost, time + tTime);

        }
    }
    int ans = MAX;
    for (int i = 0; i <= m; i++)
        ans = min(ans, cost[i][n]);
    if (ans == MAX) printf("Poor KCM\n");
    else printf("%d\n", ans);
}
int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        init();
        solution();
    }

    return 0;
}