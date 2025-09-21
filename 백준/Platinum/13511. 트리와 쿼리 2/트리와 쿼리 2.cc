#include <iostream>
#include <vector>
# define fastio cin.tie(nullptr); cout.tie(nullptr); ios_base::sync_with_stdio(false);
using namespace std;
using ll = long long;
using pii = pair<int, ll>;
ll n, m, depth[100'001], weight[17][100'001], dp[17][100'001];
vector<pii> tree[100'001];
void dfs(ll node, ll d)
{
	depth[node] = d;
	for (auto& [tnode, tw] : tree[node])
	{
		if (depth[tnode]) continue;
		dp[0][tnode] = node;
		weight[0][tnode] = tw;
		depth[tnode] = d + 1;
		dfs(tnode, d + 1);
	}
}
int main()
{
	fastio;
	cin >> n;
	for (int i = 1; i < n; ++i)
	{
		ll a, b, w;
		cin >> a >> b >> w;
		tree[a].emplace_back(b, w);
		tree[b].emplace_back(a, w);
	}
	dfs(1, 1);
	ll cnt = 0;
	for (int i = 1; i < n; i <<= 1) ++cnt;
	for (int i = 1; i < cnt; ++i)
	{
		for (int j = 1; j <= n; ++j)
		{
			dp[i][j] = dp[i - 1][dp[i - 1][j]];
			weight[i][j] = weight[i - 1][j] + weight[i - 1][dp[i - 1][j]];
		}
	}
	cin >> m;
	while (m--)
	{
		ll num, u, v, k, ans = 0, hit = 0;
		cin >> num >> u >> v;
		if (depth[u] < depth[v]) { swap(u, v); hit = 1; }
		ll a = u, b = v;
		ll diff = depth[u] - depth[v];
		ll a_diff = diff, b_diff = 0;
		for (int i = 0; diff && i < cnt; ++i)
		{
			if (diff & (1 << i))
			{
				ans += weight[i][u];
				u = dp[i][u];
			}
		}

		while (u != v)
		{
			if (dp[0][u] == dp[0][v])
			{
				++a_diff; ++b_diff;
				ans += weight[0][u] + weight[0][v];
				break;
			}
			for (int i = cnt - 1; i >= 0; --i)
			{
				if (dp[i][u] != dp[i][v])
				{
					a_diff += (1 << i); b_diff += (1 << i);
					ans += weight[i][u] + weight[i][v];
					u = dp[i][u]; v = dp[i][v];
				}
			}
		}

		if (num & 1)
			cout << ans << '\n';
		else
		{
			cin >> k;
			// hit == 1이면 b -> k로 가야함 아니면 a -> k
			if (hit)
			{
				if (k <= b_diff)
				{
					for (int i = 0; i < cnt; ++i)
						if ((k - 1) & (1 << i))
							b = dp[i][b];
					cout << b << '\n';
				}
				else
				{
					for (int i = 0; i < cnt; ++i)
						if ((a_diff + b_diff + 1 - k) & (1 << i))
							a = dp[i][a];
					cout << a << '\n';
				}
			}
			else
			{
				if (k <= a_diff)
				{
					for (int i = 0; i < cnt; ++i)
						if ((k - 1) & (1 << i))
							a = dp[i][a];
					cout << a << '\n';
				}
				else
				{
					for (int i = 0; i < cnt; ++i)
						if ((a_diff + b_diff + 1 - k) & (1 << i))
							b = dp[i][b];
					cout << b << '\n';
				}
			}
		}
	}
	return 0;
}
/*
13
1 2 1
1 3 1
2 4 1
2 5 2
3 6 2
4 7 7
4 8 5
6 9 3
8 10 2
9 11 4
10 12 6
12 13 2
*/