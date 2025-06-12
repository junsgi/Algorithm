#pragma warning(disable:4996)
#include<stdio.h>
int n, map[16][16], dp[3][16][16];
int max(int x, int y) { return x < y ? y : x; }
int inRange(int x, int y) { return 0 <= x && x < n && 0 <= y && y < n; }
/*
0 : 대각선
1 : 가로
2 : 세로

2차원 배열은 가로로 밀었는데 이전에 세로로 밀었을 때의 기록을 가지고 리턴하기 때문에 한 차원 더 필요함
dp[방향][x][y]
*/
int memo(int x, int y, int z)
{
    if (x == n - 1 && y == n - 1) return 1;
    if (dp[z][x][y]) return dp[z][x][y];

    if (z <= 1 && inRange(x, y + 1) && map[x][y + 1] != 1)
        dp[z][x][y] += memo(x, y + 1, 1);
    if (z % 2 == 0 && inRange(x + 1, y) && map[x + 1][y] != 1)
        dp[z][x][y] += memo(x + 1, y, 2);
    if (inRange(x + 1, y + 1) && map[x + 1][y] + map[x][y + 1] + map[x + 1][y + 1] == 0)
        dp[z][x][y] += memo(x + 1, y + 1, 0);
    return dp[z][x][y];
}
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n * n; i++) scanf("%d", &map[i / n][i % n]);
    printf("%d", memo(0, 1, 1));
    return 0;
}