#pragma warning(disable:4996)
#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<queue>
using namespace std;
int n, m, k, ans, matrix[50][50], tmp[50][50], mx, my;
int dire[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
queue<int> que;
void diffusion()
{
    tmp[mx][my] = tmp[mx - 1][my] = -1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            int cnt = 0;
            if (matrix[i][j] == -1) continue;
            for (const int(&d)[2] : dire)
            {
                int tx = i + d[0], ty = j + d[1];
                if (!(0 <= tx && tx < n && 0 <= ty && ty < m)) continue;
                if (matrix[tx][ty] == -1) continue;
                cnt++;
                tmp[tx][ty] += (int)floor((double)matrix[i][j] / 5);
            }
            tmp[i][j] += matrix[i][j] - (int)floor((double)matrix[i][j] / 5) * cnt;
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            matrix[i][j] = tmp[i][j];
            tmp[i][j] = 0;
        }

    }
}
void up() // 반시계
{
    int x = 0, y = 0, tx = 0, ty = 1;
    for (int _ = 0; _ < (mx + m) * 2 - 4; _++)
    {
        que.push(matrix[x][y]);
        x += tx; y += ty;
        if (x == 0 && y == m - 1) { tx = 1; ty = 0; }
        else if (x == mx - 1 && y == m - 1) { tx = 0, ty = -1; }
        else if (x == mx - 1 && y == 0) { tx = -1; ty = 0; }

    }

    x = 1; y = 0; tx = -1; ty = 0;
    for (int _ = 0; _ < (mx + m) * 2 - 4; _++)
    {
        matrix[x][y] = que.front(); que.pop();
        x += tx; y += ty;
        if (x == 0 && y == 0) { tx = 0; ty = 1; }
        else if (x == 0 && y == m - 1) { tx = 1, ty = 0; }
        else if (x == mx - 1 && y == m - 1) { tx = 0; ty = -1; }
        else if (x == mx - 1 && y == 0) { tx = -1; ty = 0; }

    }
}
void down() // 시계
{
    int x = mx, y = 0, tx = 0, ty = 1;
    for (int _ = 0; _ < (n - mx + m) * 2 - 4; _++)
    {
        que.push(matrix[x][y]);
        x += tx; y += ty;
        if (x == mx && y == m - 1) { tx = 1; ty = 0; }
        else if (x == n - 1 && y == m - 1) { tx = 0, ty = -1; }
        else if (x == n - 1 && y == 0) { tx = -1; ty = 0; }
    }
    x = mx; y = 1; tx = 0; ty = 1;
    for (int _ = 0; _ < (n - mx + m) * 2 - 4; _++)
    {
        matrix[x][y] = que.front(); que.pop();
        x += tx; y += ty;
        if (x == mx && y == m - 1) { tx = 1; ty = 0; }
        else if (x == n - 1 && y == m - 1) { tx = 0, ty = -1; }
        else if (x == n - 1 && y == 0) { tx = -1; ty = 0; }
    }
}

int main()
{
    scanf("%d%d%d", &n, &m, &k);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &matrix[i][j]);
            if (matrix[i][j] == -1)
            {
                mx = i; my = j;
            }
        }
    }
    while (k--)
    {
        diffusion();
        
        matrix[mx][my] = 0;
        matrix[mx - 1][my] = 0;
        up();
        down();
        matrix[mx][my] = -1;
        matrix[mx - 1][my] = -1;
    }
    matrix[mx - 1][my] = matrix[mx][my] = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            ans += matrix[i][j];
    printf("%d", ans);
    return 0;
}
