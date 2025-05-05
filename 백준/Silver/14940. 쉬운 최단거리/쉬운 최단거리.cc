#pragma warning(disable:4996)
#include<stdio.h>
struct Node { int x, y; };
int n, m, sx, sy, matrix[1000][1000], front, rear;
Node que[1000 * 1000];
int main()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			scanf("%d", &matrix[i][j]);
			if (matrix[i][j] == 2)
			{
				matrix[i][j] = 0;
				sx = i; sy = j;
			}
			matrix[i][j] *= -1;
		}
	}
	front = rear = -1;
	que[++rear] = { sx, sy };
	while (front != rear)
	{
		Node t = que[++front];
		int x = t.x, y = t.y;
		if (x - 1 >= 0 && matrix[x - 1][y] == -1)
		{
			que[++rear] = { x - 1, y };
			matrix[x - 1][y] = matrix[x][y] + 1;
		}

		if (x + 1 < n && matrix[x + 1][y] == -1)
		{
			que[++rear] = { x + 1, y };
			matrix[x + 1][y] = matrix[x][y] + 1;
		}

		if (y - 1 >= 0 && matrix[x][y - 1] == -1)
		{
			que[++rear] = { x, y - 1 };
			matrix[x][y - 1] = matrix[x][y] + 1;
		}

		if (y + 1 >= 0 && matrix[x][y + 1] == -1)
		{
			que[++rear] = { x, y + 1 };
			matrix[x][y + 1] = matrix[x][y] + 1;
		}
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			printf("%d ", matrix[i][j]);
		printf("\n");
	}
	return 0;
}