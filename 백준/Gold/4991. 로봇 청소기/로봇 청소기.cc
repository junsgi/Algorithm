#include <iostream>
#include <string>
using namespace std;
struct Node { int x, y, z; } que[(1 << 11) * 20 * 20];
int n, m, visit[1 << 11][20][20], cost[20][20], sx, sy, cnt, front, rear, flag;
int dire[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
string map[20];
int init()
{
    cin >> m >> n;
    if (m + n == 0) return 0;
    cnt = -1;
    for (int i = 0; i < n; i++)
    {
        cin >> map[i];
        for (int j = 0; j < m; j++)
        {
            if (map[i][j] == 'o') { map[i][j] = '.'; sx = i; sy = j; }
            if (map[i][j] == '*') { map[i][j] = ++cnt + '0'; }
        }
    }
    return 1;
}
void solution()
{
    front = rear = -1;
    que[++rear] = { sx, sy, 0 };
    visit[0][sx][sy] = ++flag;
    cost[sx][sy] = 0;
    while (front != rear)
    {
        auto& [x, y, z] = que[++front];
        if (z == (1 << cnt + 1) - 1)
        {
            cout << cost[x][y] << '\n';
            return;
        }
        for (int(&i)[2] : dire)
        {
            int tx = x + i[0], ty = y + i[1], tz = z;
            if (!(0 <= tx && tx < n && 0 <= ty && ty < m)) continue;
            if (map[tx][ty] == 'x') continue;
            if (0 <= map[tx][ty] - '0' && map[tx][ty] - '0' < 10)
                tz |= 1 << (map[tx][ty] - '0');
            if (visit[tz][tx][ty] == flag) continue;
            cost[tx][ty] = cost[x][y] + 1;
            visit[tz][tx][ty] = flag;
            que[++rear] = { tx, ty, tz };
        }
    }
    cout << -1 << '\n';
    return;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    while (init()) solution();
    return 0;
}