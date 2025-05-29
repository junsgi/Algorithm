#include<iostream>
#include<string>
using namespace std;
int n, m, sx, sy, x[600 * 600], y[600 * 600], visit[600][600], front, rear, ans;
string graph[600];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for(int i = 0 ; i < n ; i++)
    {
        cin >> graph[i];
        for(int j = 0 ; j < m ; j++)
        {
            if (graph[i][j] == 'I')
            {
                sx = i; sy = j;
            }
        }
    }
    front = rear = -1;
    visit[sx][sy] = 1;
    x[++rear] = sx;
    y[rear] = sy;
    while(front != rear)
    {
        int cx = x[++front], cy = y[front];
        if (graph[cx][cy] == 'P')
            ans++;
        if (0 <= cx + 1 && cx + 1 < n && graph[cx + 1][cy] != 'X' && !visit[cx + 1][cy])
        {
            x[++rear] = cx + 1;
            y[rear] = cy;
            visit[cx + 1][cy] = 1;
        }
        if (0 <= cx - 1 && cx - 1 < n && graph[cx - 1][cy] != 'X' && !visit[cx - 1][cy])
        {
            x[++rear] = cx - 1;
            y[rear] = cy;
            visit[cx - 1][cy] = 1;
        }
        if (0 <= cy - 1 && cy - 1 < m && graph[cx][cy - 1] != 'X' && !visit[cx][cy - 1])
        {
            x[++rear] = cx;
            y[rear] = cy - 1;
            visit[cx][cy - 1] = 1;
        }
        if (0 <= cy + 1 && cy + 1 < m && graph[cx][cy + 1] != 'X' && !visit[cx][cy + 1])
        {
            x[++rear] = cx;
            y[rear] = cy + 1;
            visit[cx][cy + 1] = 1;
        }
    }
    if (ans) cout << ans;
    else cout << "TT";
    return 0;
}