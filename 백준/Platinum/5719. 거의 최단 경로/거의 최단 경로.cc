// 거의 최단 경로란 최단 경로에 포함되지 않는 도로로만 이루어진 경로 중 가장 짧은 것
#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#define M 100000000
using namespace std;
int n, m, s, e, cost[500], visit[500], matrix[500][500];
queue<int> que;
void bfs()
{
	que = queue<int>();
	que.emplace(e);
	while (!que.empty())
	{
		int node = que.front(); que.pop();
		for (int i = 0; i < n; i++)
		{
			if (i == node || cost[node] != cost[i] + matrix[i][node]) continue; // 비용을 확인하여 최단거리만 탐색한다.
			matrix[i][node] = M; // 경로삭제
			que.emplace(i);
		}
	}
}

void dijkstra()
{
	fill(cost, cost + n, M);
	fill(visit, visit + n, 0);

	cost[s] = 0;
	int node = s, MIN = M, tnode = -1;
	for (int i = 0; i < n; i++)
	{
		if (node == -1) break;
		visit[node] = 1;
		MIN = M;
		tnode = -1;

		for (int j = 0; j < n; j++)
		{

			if (!visit[j] && cost[node] + matrix[node][j] < cost[j])
				cost[j] = cost[node] + matrix[node][j];

			if (!visit[j] && cost[j] < MIN)
			{
				MIN = cost[j];
				tnode = j;
			}
		}
		node = tnode;
	}
}
int main()
{
	while (1)
	{
		cin >> n >> m;
		if (n + m == 0) break;
		fill(&matrix[0][0], &matrix[0][0] + 500 * 500, M);
		for (int i = 0; i < n; i++) matrix[i][i] = 0;
		cin >> s >> e;
		for (int i = 0; i < m; i++)
		{
			int a, b, c;
			cin >> a >> b >> c;
			matrix[a][b] = c;
		}
		dijkstra(); // 최단경로를 구한다.
		bfs(); // e부터 시작하여 최단경로를 삭제한다.
		dijkstra(); // 거의 최단경로를 구한다.
		if (cost[e] == M) cout << -1 << '\n';
		else cout << cost[e] << '\n';

	}
	return 0;
}