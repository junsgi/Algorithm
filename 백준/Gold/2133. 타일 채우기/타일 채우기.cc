#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
using namespace std;
int n, dp[31];
int main()
{
	dp[0] = 1;
	dp[2] = 3;
	for (int i = 4; i <= 30; i += 2)
	{
		dp[i] = dp[i - 2] * dp[2];
		for (int j = i - 4; j >= 0; j -= 2)
			dp[i] += dp[j] * 2;
	}
	scanf("%d", &n);
	printf("%d", dp[n]);
	return 0;
}
/*
n >= 4
dp[n] = 3 * 2 타일 + 3 * (n - 2)
비읍모양은 2가지 이므로 n - 4부터 2를 곱한값을 더한다
*/