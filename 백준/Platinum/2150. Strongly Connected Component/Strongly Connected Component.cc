#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
# define fastio cin.tie(nullptr); cout.tie(nullptr); ios_base::sync_with_stdio(false);
using namespace std;
int n, m, visit[10'001];
vector<int> graph[10'001], graph_T[10'001];
vector<vector<int>> result;
stack<int> stk;
void dfs(int node)
{
	visit[node] = 1;
	for (const int& tnode : graph[node])
		if (!visit[tnode]) dfs(tnode);
	stk.push(node);
}
vector<int> scc(int node)
{
	visit[node] = 0;
	vector<int> res = {node};
	for (const int& tnode : graph_T[node])
	{
		if (visit[tnode])
		{
			for (int& j : scc(tnode))
				res.push_back(j);
		}
	}
	return res;
}
int main()
{
	fastio;
	cin >> n >> m;
	while (m--)
	{
		int st, ed;
		cin >> st >> ed;
		graph[st].push_back(ed);
		graph_T[ed].push_back(st);
	}
	for (int i = 1; i <= n; ++i)
		if (!visit[i])
			dfs(i);
	while (!stk.empty())
	{
		int node = stk.top(); stk.pop();
		if (!visit[node]) continue;
		result.emplace_back(scc(node));
		sort(result.back().begin(), result.back().end());
	}
	sort(result.begin(), result.end(), [](const auto& x, const auto& y) { return x[0] < y[0]; });
	cout << result.size() << '\n';
	for (vector<int>& i : result)
	{
		for (int& j : i)
			cout << j << ' ';
		cout << "-1\n";
	}
	return 0;
}