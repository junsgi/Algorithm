#include <iostream>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
int n, m, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, ans = 0x7fffffff;
int matrix[101][101], path[101][101];
int check(int avoid, int x, int y)
{
    if (avoid) // 1이면 b를 피함
        return bx1 == x && by1 == y || bx2 == x && by2 == y;
    else // 0이면 a를 피함
        return ax1 == x && ay1 == y || ax2 == x && ay2 == y;
}
void back(int idx, int* x, int* y, int* z)
{
    if (idx == -1) return;
    back(z[idx], x, y, z);
    path[x[idx]][y[idx]] = 1;
}
int bfs(int sx, int sy, int targetX, int targetY, int avoid)
{
    for (int i = 0; i <= n; i++) for (int j = 0; j <= m; j++) matrix[i][j] = 0;

    int *x = new int[101 * 101], *y = new int[101 * 101], *z = new int[101 * 101], front, rear;
    front = rear = -1;
    x[++rear] = sx;
    y[rear] = sy;
    z[rear] = -1;
    matrix[sx][sy] = 1;
    while (front != rear)
    {
        int cx = x[++front];
        int cy = y[front];
        if (cx == targetX && cy == targetY)
        {
            back(front, x, y, z);
            delete[] x;
            delete[] y;
            delete[] z;
            return matrix[cx][cy] - 1;
        }
        if (0 <= cx - 1 && !matrix[cx - 1][cy] && !path[cx - 1][cy] && !check(avoid, cx - 1, cy))
        {
            x[++rear] = cx - 1; y[rear] = cy; z[rear] = front;
            matrix[cx - 1][cy] = matrix[cx][cy] + 1;
        }
        if (cx + 1 <= n && !matrix[cx + 1][cy] && !path[cx + 1][cy] && !check(avoid, cx + 1, cy))
        {
            x[++rear] = cx + 1; y[rear] = cy; z[rear] = front;
            matrix[cx + 1][cy] = matrix[cx][cy] + 1;
        }
        if (0 <= cy - 1 && !matrix[cx][cy - 1] && !path[cx][cy - 1] && !check(avoid, cx, cy - 1))
        {
            x[++rear] = cx; y[rear] = cy - 1; z[rear] = front;
            matrix[cx][cy - 1] = matrix[cx][cy] + 1;
        }
        if (cy + 1 <= m && !matrix[cx][cy + 1] && !path[cx][cy + 1] && !check(avoid, cx, cy + 1))
        {
            x[++rear] = cx; y[rear] = cy + 1; z[rear] = front;
            matrix[cx][cy + 1] = matrix[cx][cy] + 1;
        }
    }
    delete[] x;
    delete[] y;
    delete[] z;
    return 0;
}
int main()
{
    fastio;
    cin >> n >> m >> ax1 >> ay1 >> ax2 >> ay2 >> bx1 >> by1 >> bx2 >> by2;
    int ahit = bfs(ax1, ay1, ax2, ay2, 1);
    int bhit = bfs(bx1, by1, bx2, by2, 0);
    if (ahit && bhit)
        ans = min(ans, ahit + bhit);

    for (int i = 0; i <= n; i++) for (int j = 0; j <= m; j++) path[i][j] = 0;
    bhit = bfs(bx1, by1, bx2, by2, 0);
    ahit = bfs(ax1, ay1, ax2, ay2, 1);
    if (ahit && bhit)
        ans = min(ans, ahit + bhit);

    if (ans == 0x7fffffff)
        cout << "IMPOSSIBLE";
    else
        cout << ans;
    return 0;
}