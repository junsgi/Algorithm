#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
using namespace std;
int n, m, ans, p[500000];
int find(int node)
{
	if (node == p[node]) return node;
	return p[node] = find(p[node]);
}
void Union(int x, int y)
{
	int fx = find(x), fy = find(y);
	p[fx] = fy;
}
int main()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) p[i] = i;
	for (int i = 1; i <= m; i++)
	{
		int a, b;
		scanf("%d%d", &a, &b);

		// 이미 같은 그룹에 속해있다면 사이클 발생
		if (ans == 0 && find(a) == find(b))
			ans = i;
		Union(a, b);

	}
	printf("%d", ans);
	return 0;
}
