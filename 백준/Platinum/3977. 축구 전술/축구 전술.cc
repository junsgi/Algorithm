#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#define fastio cin.tie(nullptr); cout.tie(nullptr); ios_base::sync_with_stdio(false);
using namespace std;
int t, n, m, x, y;
int visit[100'000];
vector<int> graph[100'000], graph_T[100'000];
vector<int> scc;
stack<int> stk;
queue<int> que;
void dfs(int node)
{
	visit[node] = 1;
	for (int& tnode : graph[node])
		if (!visit[tnode])
			dfs(tnode);
	stk.push(node);
}
vector<int> make_scc(int node)
{
	visit[node] = 0;
	vector<int> res = { node };
	for (int& tnode : graph_T[node])
		if (visit[tnode])
			for (int& i : make_scc(tnode))
				res.push_back(i);
	return res;
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
			cin >> x >> y;
			graph[x].push_back(y);
			graph_T[y].push_back(x);
		}
		for (int node = 0; node < n; ++node)
			if (!visit[node])
				dfs(node);
		
		scc = make_scc(stk.top());
		fill(visit, visit + n, 0);
		int hit = 0;
		visit[stk.top()] = 1;
		que.push(stk.top());
		for(int i = 0 ; i < n ; ++i)
		{
			if (que.empty())
			{
				hit = 1;
				break;
			}
			int node = que.front(); que.pop();
			for (int& tnode : graph[node])
			{
				if (visit[tnode]) continue;
				visit[tnode] = 1;
				que.push(tnode);
			}
		}
		if (hit) cout << "Confused\n";
		else
		{
			sort(scc.begin(), scc.end());
			for (int& i : scc) cout << i << '\n';
		}
		cout << '\n';
		for (int i = 0; i < n; ++i)
		{
			graph[i].clear();
			graph_T[i].clear();
			visit[i] = 0;
		}
		que = queue<int>();
		stk = stack<int>();
	}
	return 0;
}// 나폴레온 힐 성공의 법칙
