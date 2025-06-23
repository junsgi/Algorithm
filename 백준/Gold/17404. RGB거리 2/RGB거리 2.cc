#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
#define M 9999999
using namespace std;
int n, ans, matrix[1000][3], dp[1000][3];
void pro()
{
	for (int i = 1; i < n; i++)
	{
		dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + matrix[i][0];
		dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + matrix[i][1];
		dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + matrix[i][2];
	}
}
int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d%d%d", &matrix[i][0], &matrix[i][1], &matrix[i][2]);
		dp[i][0] = dp[i][1] = dp[i][2] = M;
	}
	ans = M;
	// Red 선택
	dp[0][0] = matrix[0][0];
	pro();
	// 마지막 집은 Green or Blue
	ans = min(ans, min(dp[n - 1][1], dp[n - 1][2]));

	// Greeen 선택
	dp[0][0] = M; dp[0][1] = matrix[0][1];
	pro();
	// 마지막 집은 Red or Blue
	ans = min(ans, min(dp[n - 1][0], dp[n - 1][2]));


	// Blue 선택
	dp[0][1] = M; dp[0][2] = matrix[0][2];
	pro();
	// 마지막 집은 Red or Green
	ans = min(ans, min(dp[n - 1][0], dp[n - 1][1]));

	printf("%d", ans);
	return 0;
}
