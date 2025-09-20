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
		s = 0;
		while (n)
		{
			if (n & 1) // 홀수일 때 점프, 결국 어느 숫자든 n은 1로 결정되기 때문에 x에는 최종값이 대입됨
				x = dp[s][x];
			++s;
			n >>= 1;
		}
		cout << x << '\n';

	}
	return 0;
}