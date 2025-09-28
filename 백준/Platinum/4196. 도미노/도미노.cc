#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#define fastio cin.tie(nullptr); cout.tie(nullptr); ios_base::sync_with_stdio(false);
using namespace std;
int t, n, m, visit[100'001];
vector<int> graph[100'001];
stack<int> stk;
queue<int> que;
void dfs(int node)
{
	visit[node] = 1;
	for (const int& tnode : graph[node])
		if (!visit[tnode]) dfs(tnode);
	stk.push(node);
}
int main()
{
	fastio;
	cin >> t;
	while (t--)
	{
		cin >> n >> m;
		while (m--)
		{
			int st, ed;
			cin >> st >> ed;
			graph[st].push_back(ed);
		}
		for (int i = 1; i <= n; ++i)
			if (!visit[i])
				dfs(i);
		int ans = 0;
		while (!stk.empty())
		{
			int node = stk.top(); stk.pop();
			if (!visit[node]) continue;
			que.push(node);
			visit[node] = 0;
			ans++;
			while (!que.empty())
			{
				int cur = que.front(); que.pop();
				for (int& next : graph[cur])
				{
					if (!visit[next]) continue;
					visit[next] = 0;
					que.push(next);
				}
			}
		}
		cout << ans << '\n';
		for (int i = 1; i <= n; ++i) graph[i].clear();
	}
	return 0;
}// 나폴레온 힐 성공의 법칙
