#pragma warning(disable:4996)
#include <stdio.h>
#include <algorithm>
using namespace std;
int n, m, ans;
int tetromino[510][510];
int freq[510][510];
int dire[2][4] = {{ -1, 1, 0, 0 }, { 0, 0, -1, 1 }};

void search(int x, int y, int cnt, int cost) 
{
	if (cnt == 4)
	{
		ans = ans < cost ? cost : ans;
		return;
	}
	for (int i = 0; i < 4; i++)
	{
		if (x + dire[0][i] > n || y + dire[1][i] > m) continue;
		if (x + dire[0][i] < 1 || y + dire[1][i] < 1) continue;
		if (freq[x + dire[0][i]][y + dire[1][i]]) continue;
		
		freq[x + dire[0][i]][y + dire[1][i]] = 1;
		search(x + dire[0][i], y + dire[1][i], cnt + 1, cost + tetromino[x + dire[0][i]][y + dire[1][i]]);
		freq[x + dire[0][i]][y + dire[1][i]] = 0;
	}
}

// ㅗ 모양
void cat()
{
	int s = 0;
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			s = tetromino[i][j];
			// 상
			if (i - 1 >= 1 && j + 1 <= m && j - 1 >= 1)
			{
				s += tetromino[i - 1][j];
				s += tetromino[i][j + 1];
				s += tetromino[i][j - 1];
				ans = ans < s ? s : ans;
			}


			s = tetromino[i][j];
			// 하
			if (i + 1 <= n && j + 1 <= m && j - 1 >= 1)
			{
				s += tetromino[i + 1][j];
				s += tetromino[i][j + 1];
				s += tetromino[i][j - 1];
				ans = ans < s ? s : ans;

			}

			s = tetromino[i][j];
			// 좌
			if (i + 1 <= n && i - 1 >= 1 && j - 1 >= 1)
			{
				s += tetromino[i + 1][j];
				s += tetromino[i - 1][j];
				s += tetromino[i][j - 1];
				ans = ans < s ? s : ans;
			}


			s = tetromino[i][j];
			// 우
			if (i + 1 <= n && i - 1 >= 1 && j + 1 <= m)
			{
				s += tetromino[i + 1][j];
				s += tetromino[i - 1][j];
				s += tetromino[i][j + 1];
				ans = ans < s ? s : ans;
			}

		}
	}
}
int main()
{
	scanf("%d%d", &n, &m);
	for (int i = 1; i <= n; i++) 
		for (int j = 1; j <= m; j++) 
			scanf("%d", &tetromino[i][j]);
	
	cat();
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			freq[i][j] = 1;
			search(i, j, 1, tetromino[i][j]);
			freq[i][j] = 0;
		}
	}
	printf("%d", ans);
	return 0;
}