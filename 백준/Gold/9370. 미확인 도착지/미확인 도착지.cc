// S -> G -> F -> target
// S -> F -> G -> target 경우의 수를 모두 구한다.
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
constexpr int M = 1'000'000'000;
struct Node 
{
    int node, _cost, hit;
    bool operator>(const Node& other) const {
        return _cost > other._cost;
    }
    Node(int a, int b, int c) : node(a), _cost(b), hit(c) {}
};
int T, n, m, t, s, g, f, cost[3][2001];
vector<int> target;
vector<pair<int, int>> graph[2001];
priority_queue<Node, vector<Node>, greater<Node>> heap;
void solution()
{
    cost[0][s] = 0; // 시작점에서부터
    cost[1][g] = 0; // g부터
    cost[2][f] = 0; // f부터
    heap.emplace(s, 0, 0);
    heap.emplace(g, 0, 1);
    heap.emplace(f, 0, 2);
    while (!heap.empty())
    {
        auto [node, _cost, hit] = heap.top(); heap.pop();
        if (cost[hit][node] < _cost) continue;
        for (const auto& [tnode, tcost] : graph[node])
        {
            if (cost[hit][tnode] <= cost[hit][node] + tcost) continue;
            cost[hit][tnode] = cost[hit][node] + tcost;
            heap.emplace(tnode, cost[hit][tnode], hit);
        }
    }
    for (int& i : target)
    {
        // S -> G -> F -> target
        if (cost[0][i] == cost[0][g] + cost[1][f] + cost[2][i]) cout << i << ' ';
        // S -> F -> G -> target
        else if (cost[0][i] == cost[0][f] + cost[2][g] + cost[1][i]) cout << i << ' ';
    }

    cout << '\n';
}
void reset()
{
    fill(&cost[0][0], &cost[0][0] + 3 * 2001, M);
    for (int i = 1; i <= n; i++) graph[i].clear();
    target = vector<int>(t);
}
void init()
{
    cin >> n >> m >> t;
    cin >> s >> g >> f;
    reset();
    for (int i = 0; i < m; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].emplace_back(b, c);
        graph[b].emplace_back(a, c);
    }
    for (int i = 0; i < t; i++)
        cin >> target[i];
    sort(target.begin(), target.end());
}
int main()
{
    fastio;
    cin >> T;
    while (T--)
    {
        init();
        solution();
        
    }
    return 0;
}