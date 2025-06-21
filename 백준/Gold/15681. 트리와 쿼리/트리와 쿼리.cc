#pragma warning(disable:4996)
#include<stdio.h>
#include<vector>
using namespace std;
int n, root, q, depth[100001];
vector<int> graph[100001];
int dfs(int node)
{
	if (graph[node].size() == 0)
		return 0;
	depth[node] = 1;
	for (const int& tnode : graph[node])
	{
		if (depth[tnode]) continue;
		depth[node] += dfs(tnode);
	}
	return depth[node];
}
int main()
{
	scanf("%d%d%d", &n, &root, &q);
	for (int i = 0; i < n - 1; i++)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		graph[a].push_back(b);
		graph[b].push_back(a);
	}
	dfs(root);
	for (int i = 0; i < q; i++)
	{
		int a;
		scanf("%d", &a);
		printf("%d\n", depth[a]);
	}
	return 0;
}
