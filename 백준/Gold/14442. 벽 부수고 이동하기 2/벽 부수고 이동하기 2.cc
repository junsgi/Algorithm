#include <iostream>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
constexpr int SIZE = 11 * 1000 * 1000;
int n, m, k, visit[11][1000][1000], dir[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
char map[1000][1011];
int main()
{
    fastio;
    cin >> n >> m >> k;
    for (int i = 0; i < n; ++i)
        cin >> map[i];
    int* x = new int[SIZE], *y = new int[SIZE], *z = new int[SIZE];
    int front, rear;
    front = rear = -1;
    x[++rear] = 0; y[rear] = 0; z[rear] = 0;
    visit[0][0][0] = 1;
    while (front != rear)
    {
        int cx = x[++front], cy = y[front], cz = z[front];
        int depth = visit[cz][cx][cy];
        if (cx == n - 1 && cy == m - 1)
        {
            cout << depth;
            delete[] x; delete[] y; delete[] z;
            return 0;
        }
        for (const int (&i)[2] : dir)
        {
            int tx = cx + i[0], ty = cy + i[1], tz = cz;
            if (!(0 <= tx && tx < n && 0 <= ty && ty < m)) continue;
            if (map[tx][ty] == '1' && tz + 1 <= k && !visit[tz + 1][tx][ty])
            {
                visit[tz + 1][tx][ty] = depth + 1;
                x[++rear] = tx, y[rear] = ty, z[rear] = tz + 1;
            }
            if (map[tx][ty] == '0' && !visit[tz][tx][ty])
            {
                visit[tz][tx][ty] = depth + 1;
                x[++rear] = tx, y[rear] = ty, z[rear] = tz;
            }
        }
    }
    cout << -1;
    delete[] x; delete[] y; delete[] z;
    return 0;
}
