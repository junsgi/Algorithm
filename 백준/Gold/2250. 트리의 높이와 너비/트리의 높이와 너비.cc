#pragma warning(disable:4996)
#include<stdio.h>
#include<vector>
using namespace std;
int n, level[10'001], check[10'001], c, answer = 1, m = 1;
vector<int> graph[10'001];
void inorder(int node, int depth)
{
	if (node == -1) return;
	inorder(graph[node][0], depth + 1);
	c++;
	if (level[depth] == 0)
		level[depth] = c;
	else
	{
		if (m < c - level[depth] + 1 || (m == c - level[depth] + 1 && depth + 1 < answer))
		{
			m = c - level[depth] + 1;
			answer = depth + 1;
		}
	}
	inorder(graph[node][1], depth + 1);

}
int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		int a, b, c;
		scanf("%d%d%d", &a, &b, &c);
		graph[a].emplace_back(b);
		graph[a].emplace_back(c);
		check[b]++;
		check[c]++;
	}
	for (int i = 1; i <= n; i++)
	{
		if (!check[i])
		{
			inorder(i, 0);
			break;
		}
	}
	printf("%d %d", answer, m);
	return 0;
}
