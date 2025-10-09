#include<iostream>
using namespace std;
int n, m, cnt, ans, map[500][500], x[500 * 500], y[500 * 500];
int front, rear;
int main()
{
    cin.tie(nullptr); cout.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cin >> n >> m;
    for(int i = 0 ; i < n * m ; ++i) cin >> map[i / m][i % m];
    for(int i = 0 ; i < n ; ++i)
    {
        for(int j = 0 ; j < m ; ++j)
        {
            if (!map[i][j]) continue;
            ++cnt;
            front = rear = -1;
            int c = 0;
            x[++rear] = i;
            y[rear] = j;
            map[i][j] = 0;
            while(front != rear)
            {
                int cx = x[++front], cy = y[front];
                ++c;
                if (cx - 1 >= 0 && map[cx - 1][cy])
                {
                    map[cx- 1][cy] = 0;
                    x[++rear] = cx - 1; y[rear] = cy;
                }
                if (cx + 1 < n && map[cx + 1][cy])
                {
                    map[cx + 1][cy] = 0;
                    x[++rear] = cx + 1; y[rear] = cy;
                }
                if (cy - 1 >= 0 && map[cx][cy - 1])
                {
                    map[cx][cy - 1] = 0;
                    x[++rear] = cx; y[rear] = cy - 1;
                }
                if (cy + 1 < m && map[cx][cy + 1])
                {
                    map[cx][cy + 1] = 0;
                    x[++rear] = cx; y[rear] = cy + 1;
                }
            }
            ans = max(ans, c);
        }
    }
    cout << cnt << '\n' << ans;
    return 0;
}