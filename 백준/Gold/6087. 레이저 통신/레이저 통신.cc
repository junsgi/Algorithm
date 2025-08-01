#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <iomanip>
using namespace std;
struct Node 
{
    int x, y, z, cost; 
    Node(int a, int b, int c, int d) : x{ a }, y{ b }, z{ c }, cost{ d } {}
    bool operator>(const Node& other) const {
        return cost > other.cost;
    }
};
constexpr int MAX = 1 << 13;
priority_queue<Node, vector<Node>, greater<Node>> que;
int t, n, m, cost[4][100][100], px[2], py[2], visit[4][100][100];
int dire[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
string map[100], tmp;
void init()
{
    cin >> m >> n;
    int ix = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> map[i];
        for (int j = 0; j < m; j++)
            if (map[i][j] == 'C') 
                px[ix] = i, py[ix++] = j, map[i][j] = '.';
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cost[0][i][j] = cost[1][i][j] = cost[2][i][j] = cost[3][i][j] = MAX;

}
void dijkstra(int a, int b)
{
    ++t;
    for (int i = 0; i < 4; i++)
    {
        que.emplace(a, b, i, 0);
        cost[i][a][b] = 0;
        visit[i][a][b] = t;
    }
    while (!que.empty())
    {
        auto [x, y, z, c] = que.top();
        que.pop();
        if (cost[z][x][y] < c) continue;
        for (int i = 0 ; i < 4 ; i++)
        {
            int tx = x + dire[i][0], ty = y + dire[i][1], tz = i, tc = c;
            if (!(0 <= tx && tx < n && 0 <= ty && ty < m)) continue;
            if (map[tx][ty] == '*') continue;
            if (z != tz) tc++;
            if (cost[tz][tx][ty] <= tc) continue;
            que.emplace(tx, ty, tz, tc);
            cost[tz][tx][ty] = tc;
            visit[tz][tx][ty] = t;
        }
    }
}
void solution()
{
    /*for (int k = 0; k < 4; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
                cout << setw(5) << (cost[k][i][j] == MAX) ? -1 : cost[k][i][j];
            cout << '\n';
        }
        cout << "\n\n";
    }*/
    

    int ans = MAX;
    for (int k = 0; k < 4; k++)
    {
        //cout << cost[k][px[1]][py[1]] << '\n';
        if (visit[k][px[1]][py[1]])
            ans = min(ans, cost[k][px[1]][py[1]]);
    }
        
    cout << ans;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    init();
    dijkstra(px[0], py[0]);
    solution();
    
    return 0;
}
/*
11 5
...*...*...
.*.*.*.*.*.
.*.*.*.*.*.
.*.*.*.*.*.
C*...*...*C
*/