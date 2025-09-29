#include <iostream>
#include <algorithm>
using namespace std;
int t, n, dp[10'001];
int main()
{
	cin.tie(nullptr); cout.tie(nullptr);
	ios_base::sync_with_stdio(false);

	for (int i = 0; i <= 10'000; ++i)
		dp[i] = 1;
	for (int i = 2; i <= 10'000; ++i)
		dp[i] += dp[i - 2];
	for (int i = 3; i <= 10'000; ++i)
		dp[i] += dp[i - 3];
	cin >> t;
	while (t--)
	{
		cin >> n;
		cout << dp[n] << '\n';
	}
	return 0;
}
