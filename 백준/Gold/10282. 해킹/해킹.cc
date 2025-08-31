#include <iostream>
#include <vector>
#include <queue>
using namespace std;
constexpr int M = 20'000'000;
int t, n, d, c, a, b, s, cost[10'001];
vector<pair<int, int>> graph[10'001];
priority_queue<pair<int, int>> heap;
int main()
{
    cin.tie(nullptr); cout.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cin >> t;
    while (t--)
    {
        cin >> n >> d >> c;
        for (int i = 1; i <= n; ++i)
        {
            graph[i].clear();
            cost[i] = M;
        }
        heap = priority_queue<pair<int, int>>();
        for (int i = 0; i < d; ++i)
        {
            cin >> a >> b >> s;
            graph[b].emplace_back(a, s);
        }
        cost[c] = 0;
        heap.emplace(0, c);
        while (!heap.empty())
        {
            const auto [_cost, node] = heap.top();
            heap.pop();
            if (cost[node] < -_cost) continue;
            for (const auto& [tnode, tcost] : graph[node])
            {
                if (cost[tnode] <= -_cost + tcost) continue;
                cost[tnode] = -_cost + tcost;
                heap.emplace(-(-_cost + tcost), tnode);
            }
        }
        int cnt = 0, ans = 0;
        for (int i = 1; i <= n; i++)
        {
            if (cost[i] == M) continue;
            ++cnt;
            ans = max(ans, cost[i]);
        }
        cout << cnt << ' ' << ans << '\n';
    }

    return 0;
}
