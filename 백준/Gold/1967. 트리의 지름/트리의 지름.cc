#include<stdio.h>
#include<vector>
using namespace std;
struct Temp { int node, w; };
int n, ans;
vector<struct Temp> tree[10'001];
int dfs(int node)
{
	if (tree[node].size() == 0) return 0;
	int m1 = 0, m2 = 0;
	for (Temp& t : tree[node])
	{
		int res = dfs(t.node);
		if (m1 < res + t.w)
		{
			m2 = m1;
			m1 = res + t.w;
		}
		else
			m2 = m2 < res + t.w ? res + t.w : m2;
	}
	ans = ans < m1 + m2 ? m1 + m2 : ans;
	return m1;
}
int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n - 1; i++)
	{
		int a, b, c;
		scanf("%d%d%d", &a, &b, &c);
		tree[a].push_back({ b, c });
	}
	dfs(1);
	printf("%d", ans);
	return 0;
}