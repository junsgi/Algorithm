#pragma warning(disable:4996)
#include<iostream>
#include<algorithm>
#include<queue>
#include<string>
using namespace std;
int n, a, b, RG[100][100], RGB[100][100], dire[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
string graph[100];
queue<pair<int, int>> que;
void bfs(int x, int y, int(&visit)[100][100], bool(*cmp)(const char& x, const char& y))
{
    que = queue<pair<int, int>>();
    que.push({ x, y });
    visit[x][y] = 1;
    while (!que.empty())
    {
        pair<int, int> cur = que.front(); que.pop();

        for (const int(&i)[2] : dire)
        {
            int tx = cur.first + i[0], ty = cur.second + i[1];
            if (!(0 <= tx && tx < n && 0 <= ty && ty < n)) continue;
            if (visit[tx][ty] || !cmp(graph[cur.first][cur.second], graph[tx][ty])) continue;
            visit[tx][ty] = 1;
            que.push({ tx, ty });
        }
    }
}
bool rgb(const char& x, const char& y)
{
    return x == y;
}
bool rg(const char& x, const char& y)
{
    return rgb(x, y) || (x == 'R' && y == 'G') || (x == 'G' && y == 'R');
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> graph[i];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (RGB[i][j] == 0)
            {
                a++;
                bfs(i, j, RGB, rgb);
            }
            if (RG[i][j] == 0)
            {
                b++;
                bfs(i, j, RG, rg);
            }
        }
    }
    cout << a << " " << b;
    return 0;
}