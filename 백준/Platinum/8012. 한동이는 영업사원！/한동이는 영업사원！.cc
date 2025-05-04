// 공통조상찾기 문제
#pragma warning(disable:4996)
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
int n, m, ex, a, b, ans, node, dp[16][30'000], depth[30000], visit[30000], power[16];
vector<int> graph[30'000];
void dfs(int x, int d)
{
	visit[x] = 1;
	depth[x] = d;
	for (const int tnode : graph[x])
	{
		if (visit[tnode]) continue;
		dp[0][tnode] = x;
		dfs(tnode, d + 1);
	}
}
int main()
{
	cin >> n;
	power[0] = 1;
	for (int i = 1; i < n; i *= 2) ex++;
	for (int i = 0; i < n - 1; i++)
	{
		cin >> a >> b;
		a--; b--;
		graph[a].emplace_back(b);
		graph[b].emplace_back(a);
	}
	dfs(0, 0);
	for (int i = 1; i <= ex; i++)
		for (int j = 0; j < n; j++)
			dp[i][j] = dp[i - 1][dp[i - 1][j]];
	cin >> n;
	node = 0;
	for (int i = 0; i < n; i++)
	{
		cin >> m; m--;
		a = node;
		b = m;
		if (depth[a] > depth[b])
		{
			a = m;
			b = node;
		}
		int diff = depth[b] - depth[a];
		for (int j = ex; j >= 0; j--)
		{
			if (diff & (1 << j))
			{
				b = dp[j][b];
				ans += (1 << j);
			}
		}

		while (a != b)
		{
			if (dp[0][a] == dp[0][b])
			{
				ans += 2;
				break;
			}
			for (int i = ex; i >= 0; i--)
			{
				if (dp[i][a] == dp[i][b])continue;
				a = dp[i][a];
				b = dp[i][b];
				ans += (1 << i) * 2;
			}
		}
		node = m;
	}
	cout << ans;
	return 0;
}