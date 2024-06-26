#pragma warning(disable:4996)
#include<stdio.h>
#include<vector>
#include<string>
#define MAX 100'001
using namespace std;
int n, t, root, ed, ec,ans, visit[MAX];
int max(int a, int b) { return a < b ? b : a; }
int min(int a, int b) { return a > b ? b : a; }
vector<pair<int, int>> graph[MAX];
/*
트리의 지름 구하기
1. 아무 노드 선택
2. 가장 먼 거리에 있는 노드 선택 (DFS)
3. 선택한 노드에서 다시 DFS 탐색하여 지름을 구함
*/
void DFS(int node, int cost, int chk)
{
	if (cost > ec)
	{
		ed = node;
		ec = cost;
	}
	visit[node] = chk;
	for (int i = 0; i < (int)graph[node].size(); i++)
	{
		int tnode = graph[node][i].first;
		int tcost = graph[node][i].second;
		if (visit[tnode] == chk) continue;
		DFS(tnode, cost + tcost, chk);
	}
}
int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &root);
		for (int j = 0; ; j++)
		{
			scanf("%d", &t);
			if (t == -1) break;
			if (j % 2 == 0)
				graph[root].push_back({ t, 0 });
			else
				graph[root][(int)graph[root].size() - 1].second = t;
		}
	}
	DFS(root, 0, 1);
	ec = 0;
	DFS(ed, 0, 2);
	printf("%d", ec);
	return 0;
}
