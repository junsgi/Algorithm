#include <iostream>
# define fastio cin.tie(nullptr); cout.tie(nullptr); ios_base::sync_with_stdio(false);
using namespace std;
int m, q, n, x, s, dp[20][200'001];
int main()
{
	fastio;
	cin >> m;
	for (int i = 1; i <= m; ++i)
		cin >> dp[0][i];
	for (int i = 1; i < 20; ++i)
		for (int j = 1; j <= m; ++j)
			dp[i][j] = dp[i - 1][dp[i - 1][j]];
	cin >> q;
	while (q--)
	{
		cin >> n >> x; 
		for (int i = 0; i < 20; ++i)
			if (n & (1 << i))
				x = dp[i][x];
		cout << x << '\n';
	}
	return 0;
}