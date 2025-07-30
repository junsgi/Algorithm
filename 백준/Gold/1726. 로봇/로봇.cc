#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
int n, m, sx,sy,sw, ex,ey,ew;
int map[101][101], che[5][101][101];
int dire[2][5] = {{0, 0, 0, 1, -1}, {0, 1, -1, 0, 0}}; // 1: 동, 2:서, 3:남, 4:북
int ttt[5][2] = {{0,0}, {3, 4}, {3, 4}, {1, 2}, {1, 2}};
struct temp{int x, y, w;}t;
queue<temp> que;
int main()
{
	scanf("%d%d", &n, &m);
	for(int i = 1 ; i <= n ; i++)
		for(int j = 1 ; j <= m ; j++)
			scanf("%d", &map[i][j]);
	scanf("%d%d%d%d%d%d", &sx,&sy,&sw,&ex,&ey,&ew);
	t.x = sx; t.y = sy ; t.w = sw;

	que.push(t);

	while (!que.empty())
	{
		temp tmp = que.front();
		if (tmp.x == ex && tmp.y == ey && tmp.w == ew)
		{
			printf("%d", che[tmp.w][tmp.x][tmp.y]);
			return 0;
		}
		que.pop();

		for(int d = 0 ; d < 2 ; d++)
		{
			if (!che[ttt[tmp.w][d]][tmp.x][tmp.y])
			{
				che[ttt[tmp.w][d]][tmp.x][tmp.y] = che[tmp.w][tmp.x][tmp.y] + 1;
				t.x = tmp.x; t.y = tmp.y ; t.w = ttt[tmp.w][d];
				que.push(t);
			}
		}
		
		// 현재 바라보고 있는 방향으로 d 칸 이동
		for(int d = 1 ; d <= 3 ; d++)
		{
			int tx = dire[0][tmp.w] * d + tmp.x;
			int ty = dire[1][tmp.w] * d + tmp.y;
			if (tx <= 0 || tx > n || ty <= 0 || ty > m) continue; // d칸 이동했을 때 범위를 벗어난다면
			if (map[tx][ty]) break; // 궤도가 없다면
			if (che[tmp.w][tx][ty]) continue; // 참조한 적 있다면
			t.x = tx ; t.y = ty ; t.w = tmp.w;
			che[tmp.w][tx][ty] = che[tmp.w][tmp.x][tmp.y] + 1;
			que.push(t);
		}
	}
	return 0;
}