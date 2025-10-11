#include <stdio.h>
#include <stdlib.h>
#include <queue>
#include <algorithm>
using namespace std;
int n, area, st1, st2, ed1, ed2;
int dire[2][8] = {{-1, -2, -2, -1, 1, 2, 2, 1}, {-2, -1, 1, 2, -2, -1, 1, 2}};
int freq[500][500];
struct temp
{
	int x, y, depth;
};
void BFS()
{
	queue<temp> que;
	temp t;

	freq[st1][st2] = 1;
	t.x = st1;
	t.y = st2;
	t.depth = 0;
	que.push(t);

	while(!que.empty())
	{
		t = que.front();
		que.pop();
		if (t.x == ed1 && t.y == ed2) {printf("%d\n", t.depth); return; }

		for(int i = 0 ; i < 8 ; i++)
		{
			temp tmp;
			tmp.x = t.x + dire[0][i];
			tmp.y = t.y + dire[1][i];
			tmp.depth = t.depth + 1;
			if (tmp.x < 0 || tmp.x >= area) continue;
			if (tmp.y < 0 || tmp.y >= area) continue;
			if (freq[tmp.x][tmp.y]) continue;
			freq[tmp.x][tmp.y] = 1;
			que.push(tmp);

		}
	}
}

int main()
{
	scanf("%d", &n);
	for(int i = 0 ; i < n ; i++)
	{
		scanf("%d%d%d%d%d", &area, &st1, &st2, &ed1, &ed2);
		BFS();
		fill(&freq[0][0], &freq[400][400], 0);
	}
	return 0;
}
