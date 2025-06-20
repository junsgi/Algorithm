#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
using namespace std;
int m, n, c[20], p[20], dp[1101];
int min(int a, int b) { return a < b ? a : b; }
int main()
{
	scanf("%d%d", &m, &n);
	for (int i = 0; i < n; i++)
		scanf("%d%d", &c[i], &p[i]);
	for (int i = 1; i < m + 101; i++) dp[i] = 9999999;
	for (int i = 0; i < n; i++)
		for (int j = 1; j <= m + 100; j++)
			if (p[i] <= j)
				dp[j] = min(dp[j], dp[j - p[i]] + c[i]);
	int ans = 9999999;
	for (int i = m; i <= m + 100; i++)
		ans = min(ans, dp[i]);
	printf("%d", ans);
	return 0;
}
