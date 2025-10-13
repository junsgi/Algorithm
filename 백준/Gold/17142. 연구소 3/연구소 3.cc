#include<iostream>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;
struct Node 
{
    int x, y, d;
    Node(int a, int b, int c) : x{ a }, y{ b }, d{ c } {}
};
int n, m, map[50][50], visit[50][50], space, ans = 2501, cnt;
int dire[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
vector<pair<int, int>> virus;
vector<int> ck;
queue<Node> que;
void bfs()
{
    int second = 0, sp = space;
    while (!que.empty())
    {
        auto [x, y, d] = que.front(); que.pop();
        if (map[x][y] == 0)
        {
            --sp;
            second = max(second, d);
        }
        for (int(&i)[2] : dire)
        {
            int tx = x + i[0], ty = y + i[1];
            if (!(0 <= tx && tx < n && 0 <= ty && ty < n)) continue;
            if (map[tx][ty] == 1) continue;
            if (visit[tx][ty] == cnt) continue;
            visit[tx][ty] = cnt;
            que.emplace(tx, ty, d + 1);
        }
    }
    if (!sp)
        ans = min(ans, second);

}
void choice(int idx, int depth)
{
    if (depth == m)
    {
        ++cnt;
        for (int i = 0; i < ck.size(); ++i)
        {
            if (!ck[i]) continue;
            auto& [x, y] = virus[i];
            que.emplace(x, y, 0);
            visit[x][y] = cnt;
        }
        bfs();
        return;
    }
    for (int i = idx; i < virus.size(); ++i)
    {
        auto& [x, y] = virus[i];
        ck[i] = 1;
        choice(i + 1, depth + 1);
        ck[i] = 0;
    }
}
int main()
{
    cin.tie(nullptr); cout.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            cin >> map[i][j];
            if (!map[i][j])++space;
            if (map[i][j] == 2)
                virus.emplace_back(i, j);
        }
    }
    ck = vector<int>(virus.size(), 0);
    choice(0, 0);
    if (ans == 2501) cout << -1;
    else cout << ans;
    return 0;
}