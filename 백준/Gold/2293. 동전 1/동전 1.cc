#include<iostream>
#include<algorithm>
using namespace std;
int n, t, dp[10'001], coin[100];
int main() 
{
	cin.tie(nullptr)->sync_with_stdio(false);
	cout.tie(nullptr)->sync_with_stdio(false);
	cin >> n >> t;
	for (int i = 0; i < n; ++i)
		cin >> coin[i];
	sort(coin, coin + n);
	dp[0] = 1;
	for (int i = 0; i < n; ++i)
		for (int j = coin[i]; j <= t; ++j)
			dp[j] += dp[j - coin[i]];
	cout << dp[t];
	return 0;
}