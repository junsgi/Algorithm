#include <iostream>
#include <algorithm>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
constexpr int M = 500 * 1000;
struct Node { int x, y; }que[M];
int n, matrix[500][1000], visit[500][1000], num[500][1000], path[M], freq[500 * 500 - (500 >> 1) + 1], front, rear;
int dir[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
int inRange(int x, int y) { return 0 <= x && x < n && 0 <= y && y < (n << 1); }
void init()
{
    fastio;
    cin >> n;
    int flag = 1, m = 0;
    int r = 0, c = 0, er = 1, ec = 1;
    for (int i = 0; i < n * n - (n >> 1); i++)
    {
        int a, b;
        cin >> a >> b;
        ++m;
        if (flag)
        {
            matrix[r][c] = a;
            matrix[r][c + 1] = b;
            num[r][c] = num[r][c + 1] = m;
            c += 2;
            if (c >= (n << 1))
            {
                r += 2;
                c = 0;
                flag = 0;
            }
        }
        else
        {
            matrix[er][ec] = a;
            matrix[er][ec + 1] = b;
            num[er][ec] = num[er][ec + 1] = m;
            ec += 2;
            if (ec >= (n << 1) - 1)
            {
                er += 2;
                ec = 1;
                flag = 1;
            }
        }
    }
}
void back(int idx)
{
    if (idx == -1) return;
    back(path[idx]);
    int p = num[que[idx].x][que[idx].y];
    if (!freq[p])
    {
        cout << p << ' ';
        freq[p] = 1;
    }
}
void solution()
{
    front = rear = -1;
    que[++rear] = { 0, 0 };
    path[rear] = -1;

    que[++rear] = { 0, 1 };
    path[rear] = -1;
    visit[0][0] = visit[0][1] = 1;
    int _max = 0, _front = -1, _num = 0;
    while (front != rear)
    {
        auto [x, y] = que[++front];
        if (_max < num[x][y])
        {
            _num = visit[x][y];
            _max = num[x][y];
            _front = front;
        }
        for (const int(&i)[2] : dir)
        {
            int tx = x + i[0], ty = y + i[1];
            if (!inRange(tx, ty) || matrix[tx][ty] == 0) continue;
            if (num[x][y] != num[tx][ty] && matrix[x][y] != matrix[tx][ty]) continue;
            if (visit[tx][ty]) continue;

            visit[tx][ty] = visit[x][y] + 1;
            que[++rear] = { tx, ty };
            path[rear] = front;

            for (const int(&j)[2] : dir)
            {
                int txx = tx + j[0], tyy = ty + j[1];
                if (!inRange(txx, tyy) || matrix[txx][tyy] == 0) continue;
                if (num[tx][ty] != num[txx][tyy]) continue;
                if (visit[txx][tyy]) continue;
                que[++rear] = { txx, tyy };
                visit[txx][tyy] = visit[x][y] + 1;
                path[rear] = front;
            }
            
           
        }
    }
    cout << _num << '\n';
    back(_front);
}
int main()
{
    init();
    solution();
    return 0;
}