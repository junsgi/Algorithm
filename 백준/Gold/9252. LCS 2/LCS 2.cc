#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
using namespace std;
int i, j, dp[1001][1001];
char a[1002], b[1002];
void print(int x, int y)
{
	if (dp[x][y] == 0) return;
	if (a[x] == b[y])
	{
		print(x - 1, y - 1);
		printf("%c", a[x]);
	}
	else
		return dp[x - 1][y] < dp[x][y - 1] ? print(x, y - 1) : print(x - 1, y);
}
int main()
{
	scanf("%s", a + 1);
	scanf("%s", b + 1);

	for (i = 1; a[i]; i++)
	{
		for (j = 1; b[j]; j++)
		{
			if (a[i] == b[j]) dp[i][j] = dp[i - 1][j - 1] + 1;
			else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
		}
	}
	printf("%d\n", dp[i - 1][j - 1]);
	print(i - 1, j - 1);
	return 0;
}
