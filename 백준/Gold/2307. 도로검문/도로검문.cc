#include<stdio.h>
#include<vector>
#include<queue>
using namespace std;
typedef pair<int, int> pii;
int n, m, t1, t2, k, answer, cost[1001];
vector<pii> graph[1001], arr;
int dijkstra()
{
	for (int i = 1; i <= n; i++)
		cost[i] = 100'000'000;
	priority_queue<pii, vector<pii>, greater<pii>> que = {};
	que.emplace(0, 1);
	cost[1] = 0;
	
	while (!que.empty())
	{
		pii con = que.top(); que.pop();
		int node = con.second, weight = con.first;
		if (node == n) return weight;
		if (cost[node] < weight) continue;

		for (pii& t : graph[node])
		{
			int tnode = t.first, tw = t.second;
			if (node == t1 && tnode == t2 || node == t2 && tnode == t1) continue;
			if (cost[tnode] <= cost[node] + tw) continue;
			cost[tnode] = cost[node] + tw;
			que.emplace(cost[tnode], tnode);
		}
	}
	return -1;
}
int main()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < m; i++)
	{
		int a, b, c;
		scanf("%d%d%d", &a, &b, &c);
		graph[a].emplace_back(b, c);
		graph[b].emplace_back(a, c);
		arr.emplace_back(a, b);
	}
	k = dijkstra();
	for (pii& i : arr)
	{
		t1 = i.first; t2 = i.second;
		int res = dijkstra();
		if (res == -1)
		{
			printf("-1");
			return 0;
		}
		else
			answer = max(answer, res - k);
	}
	printf("%d", answer);
	return 0;
}
