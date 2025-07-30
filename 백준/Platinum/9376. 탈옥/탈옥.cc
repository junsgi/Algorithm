#include <iostream>
#include <string>
#include <queue>
#include <vector>
using namespace std;
struct Node 
{
    int x, y, z; 
    Node(int a, int b, int c) : x{ a }, y{ b }, z{ c } {}
    bool operator>(const Node& other) const {
        return z > other.z; 
    }
};
constexpr int MAX = 1 << 13;
priority_queue<Node, vector<Node>, greater<Node>> que;
int t, n, m, cnt, cost[3][102][102], px[2], py[2];
int dire[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
string map[102], tmp;
void init()
{
    cin >> n >> m;
    for (int i = 0; i < n + 2; i++)
        map[i] = string(m + 2, '.');
    int ix = 0;
    for (int i = 1; i <= n; i++)
    {
        cin >> tmp;
        for (int j = 1; j <= m; j++)
        {
            map[i][j] = tmp[j - 1];
            if (map[i][j] == '$') 
                px[ix] = i, py[ix++] = j, map[i][j] = '.';
        }
    }
    for (int i = 0; i < n + 2; i++)
        for (int j = 0; j < m + 2; j++)
            cost[0][i][j] = cost[1][i][j] = cost[2][i][j] = MAX;

}
void dijkstra(int p, int a, int b)
{
    que.emplace(a, b, 0);
    cost[p][a][b] = 0;
    while (!que.empty())
    {
        auto& [x, y, z] = que.top();

        if (cost[p][x][y] < z) continue;
        for (int(&i)[2] : dire)
        {
            int tx = x + i[0], ty = y + i[1], tz = z;
            if (!(0 <= tx && tx <= n + 1 && 0 <= ty && ty <= m + 1)) continue;
            if (map[tx][ty] == '*') continue;
            if (map[tx][ty] == '#') tz++;
            if (cost[p][tx][ty] <= tz) continue;
            que.emplace(tx, ty, tz);
            cost[p][tx][ty] = tz;
        }
        que.pop();
    }
}
void solution()
{
    int ans = MAX;
    for (int i = 0; i <= n + 1; i++)
    {
        for (int j = 0; j <= n + 1; j++)
        {
            if (map[i][j] == '*') continue;
            if (map[i][j] == '#')
                ans = min(ans, (cost[0][i][j] + cost[1][i][j] + cost[2][i][j]) - 2);
            else
                ans = min(ans, cost[0][i][j] + cost[1][i][j] + cost[2][i][j]);
        }
    }
    cout << ans << '\n';
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    cin >> t;
    while (t--)
    {
        init();
        dijkstra(0, 0, 0);
        dijkstra(1, px[0], py[0]);
        dijkstra(2, px[1], py[1]);
        solution();
    }
    return 0;
}
