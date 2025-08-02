#pragma warning(disable:4996)
#include <stdio.h>
#include <vector>
using namespace std;
int map[1001][1001], que[3][1001 * 1001], freq[1001][1001];
int front, rear, n, m, ans, cnt, x, y, tx,ty;
int dir[2][4] = { {0,1,0,-1}, {1,0,-1,0} };
int main()
{
    scanf("%d%d", &n, &m);
    ans = n * m;
    front = rear = -1;
    
    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            scanf("%d", &map[i][j]);
            if (map[i][j] == -1) ans -= 1;
            else if (map[i][j] == 1)
            {
                cnt++;
                que[0][++rear] = i; // x 좌표
                que[1][rear] = j; // y 좌표
                que[2][rear] = 0; // 깊이
                freq[x][y] = 1; // 중복 방지
            }
        }
    }
    if (cnt == ans)
    {
        printf("0");
        return 0;
    }
    else
    {
        while (front != rear)
        {
            tx = que[0][++front];
            ty = que[1][front];

            for (int i = 0; i < 4; i++)
            {
                if (tx + dir[0][i] <= m && tx + dir[0][i] >= 1 && ty + dir[1][i] <= n && ty + dir[1][i] >= 1 && !freq[tx + dir[0][i]][ty + dir[1][i]] && !map[tx + dir[0][i]][ty + dir[1][i]])
                {
                    que[0][++rear] = tx + dir[0][i];
                    que[1][rear] = ty + dir[1][i];
                    freq[tx + dir[0][i]][ty + dir[1][i]] = 1;
                    que[2][rear] = que[2][front] + 1;
                    cnt++;
                    if (cnt == ans)
                    {
                        printf("%d", que[2][rear]);
                        return 0;
                    }
                    
                }
            }
        }
    }
    printf("-1");
    return 0;
}
