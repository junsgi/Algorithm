#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
using namespace std;
int n, matrix[128][128], ans[3];
int pro(int x, int y, int len)
{
	if (len == 1) return matrix[x][y];
	int tlen = len / 2;
	int res1 = pro(x, y + tlen, tlen);
	int res2 = pro(x, y, tlen);
	int res3 = pro(x + tlen, y, tlen);
	int res4 = pro(x + tlen, y + tlen, tlen);
	if (res1 == res2 && res2 == res3 && res3 == res4) return res1;
	else
	{
		ans[res1]++; ans[res2]++; ans[res3]++; ans[res4]++;
		return 2;
	}
}
int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n * n; i++)
		scanf("%d", &matrix[i / n][i % n]);
	ans[pro(0, 0, n)]++;
	printf("%d\n%d", ans[0], ans[1]);
	return 0;
}