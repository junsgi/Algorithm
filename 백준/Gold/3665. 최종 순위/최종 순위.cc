#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
# define fastio cin.tie(nullptr); cout.tie(nullptr); ios_base::sync_with_stdio(false);
using namespace std;
int t, n, m, a, b;
int check[501], k[501][501], team[501], _rank[501];
vector<int> graph[501], ans;
queue<int> que;
int main()
{
	fastio;
	cin >> t;
	while (t--)
	{
		cin >> n;
		for (int i = 1; i <= n; ++i)
		{
			cin >> team[i]; // 팀 번호
			_rank[team[i]] = i;
		}
		for (int i = 1; i <= n; ++i)
		{
			for (int j = i + 1; j <= n; ++j)
			{
				k[team[i]][team[j]] = 1;
				++check[team[j]];
			}
		}
		cin >> m;
		while (m--)
		{
			cin >> a >> b;
			if (_rank[a] > _rank[b])
			{
				k[b][a] = 0; k[a][b] = 1;
				++check[b]; --check[a];
			}
			else 
			{
				k[a][b] = 0; k[b][a] = 1;
				++check[a]; --check[b];
			}
		}

		for (int i = 1; i <= n; ++i)
		{
			if (check[i] == 0)
				que.push(i);
		}
		int isFail = 0;
		for (int _ = 0 ; _ < n ; ++_)
		{
			if (que.empty())
			{
				isFail = 1;
				break;
			}
			int node = que.front(); que.pop();
			ans.push_back(node);
			for (int tnode = 1 ; tnode <= n ; ++tnode)
				if(k[node][tnode] && --check[tnode] == 0)
					que.push(tnode);
		}
		if (isFail)
			cout << "IMPOSSIBLE";
		else
			for (int& i : ans) cout << i << ' ';
		cout << '\n';

		ans.clear();
		for (int i = 1; i <= n; ++i)
		{
			graph[i].clear();
			check[i] = 0;
			for (int j = 1; j <= n; ++j)
				k[i][j] = 0;
		}
	}
	return 0;
}