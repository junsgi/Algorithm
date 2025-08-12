#include <iostream>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
struct Node { int x, y; } que[100 * 100];
int n, map[100][100], visit[100][100], cnt, dir[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
int _min = 222, _max;
int bfs(int st, int ed)
{
    if (!(st <= map[0][0] && map[0][0] <= ed)) return 0;
    int front, rear;
    front = rear = -1;
    que[++rear] = { 0, 0 };
    visit[0][0] = ++cnt;
    while (front != rear)
    {
        auto [x, y] = que[++front];
        if (x == n - 1 && y == n - 1)
            return 1;
        for (const int(&i)[2] : dir)
        {
            int tx = x + i[0], ty = y + i[1];
            if (!(0 <= tx && tx < n && 0 <= ty && ty < n)) continue;
            if (!(st <= map[tx][ty] && map[tx][ty] <= ed)) continue;
            if (visit[tx][ty] == cnt) continue;
            visit[tx][ty] = cnt;
            que[++rear] = { tx, ty };
        }
    }
    return 0;
}
int main()
{
    fastio;
    cin >> n;
    for (int i = 0; i < n * n; ++i)
    {
        cin >> map[i / n][i % n];
        _min = min(_min, map[i / n][i % n]);
        _max = max(_max, map[i / n][i % n]);
    }
    int left = 0, right = 200, mid, hit;
    while (left < right)
    {
        mid = left + right >> 1;
        hit = 0;
        for (int i = _min; i <= _max; i++)
        {
            hit = bfs(i, i + mid);
            if (hit) break;
        }
        if (hit) right = mid;
        else left = mid + 1;
    }
    cout << left;
    return 0;
}
