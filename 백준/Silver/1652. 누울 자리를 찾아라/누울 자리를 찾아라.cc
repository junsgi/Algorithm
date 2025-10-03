#include<iostream>
#include<string>
using namespace std;
int n, row, col, visit[2][100][100];
string map[100];
int inRange(int x, int y) { return 0 <= x && x < n && 0 <= y && y < n; }
int right(int x, int y, int depth)
{
    if (!inRange(x, y) || map[x][y] == 'X') return depth;
    visit[0][x][y] = 1;
    return right(x, y + 1, depth + 1);
}
int down(int x, int y, int depth)
{
    if (!inRange(x, y) || map[x][y] == 'X') return depth;
    visit[1][x][y] = 1;
    return down(x + 1, y, depth + 1);
}
int main()
{
    cin >> n;
    for (int i = 0; i < n; ++i)
        cin >> map[i];
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (!visit[0][i][j] && map[i][j] == '.')
                if (right(i, j, 0) > 1) ++row;
            if (!visit[1][i][j] && map[i][j] == '.')
                if (down(i, j, 0) > 1) ++col;
        }
    }
    cout << row << ' ' << col;
    return 0;
}