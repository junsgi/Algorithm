#pragma warning(disable:4996)
// 희소배열로 최소공동조상 찾기, 비트마스킹으로 log2(high depth - low depth)만에 위치를 찾음
#include<iostream>
#include<vector>
#include<algorithm>
#define M 20
using namespace std;
struct Node 
{
	int node, weight; 
	Node(int a, int b) : node(a), weight(b) {}
};
int n, k, ex, ck[100'000], depth[100'000], dp[M][100'000], MIN[M][100'000], MAX[M][100'000];
vector<Node> graph[100'000];
void init()
{
	cin >> n;
	for (int i = 1; i <= n; i *= 2) ex++;
	for (int i = 0; i < n - 1; i++)
	{
		int a, b, c;
		cin >> a >> b >> c; a--; b--;
		graph[a].emplace_back(b, c);
		graph[b].emplace_back(a, c);
	}
}
void dfs(int node, int d)
{
	ck[node] = 1; depth[node] = d;
	for (const Node& t : graph[node])
	{
		if (ck[t.node]) continue;
		dp[0][t.node] = node;
		MIN[0][t.node] = MAX[0][t.node] = t.weight;
		dfs(t.node, d + 1);
	}
}
void solution()
{
	dfs(0, 0);
	MIN[0][0] = 0x7fffffff;

	// 희소 배열 만듦
	for (int i = 1; i <= ex; i++)
	{
		for (int j = 0; j < n; j++)
		{
			dp[i][j] = dp[i - 1][dp[i - 1][j]];
			MIN[i][j] = min(MIN[i - 1][j], MIN[i - 1][dp[i - 1][j]]);
			MAX[i][j] = max(MAX[i - 1][j], MAX[i - 1][dp[i - 1][j]]);
		}
	}
	//print();

	cin >> k;
	for (int i = 0; i < k; i++)
	{
		int a, b, a1 = 0x7fffffff, a2 = 0;
		cin >> a >> b; a--; b--;
		if (depth[a] > depth[b]) 
			swap(a, b);
		int cnt = abs(depth[b] - depth[a]);
		for (int bit = 0; bit <= ex; bit++)
		{
			if ((cnt & (1 << bit)) == 0)
				continue;
			a1 = min(a1, MIN[bit][b]);
			a2 = max(a2, MAX[bit][b]);
			b = dp[bit][b];
		}

		while (a != b) // 높이를 맞춘 후 같은 조상 바라보고있다면 false
		{
			if (dp[0][a] == dp[0][b])
			{
				a1 = min(a1, min(MIN[0][a], MIN[0][b]));
				a2 = max(a2, max(MAX[0][a], MAX[0][b]));
				break;
			}
			for (int tx = ex; tx >= 0; tx--)
			{
				if (dp[tx][a] == dp[tx][b]) continue;
				a1 = min(a1, min(MIN[tx][a], MIN[tx][b]));
				a2 = max(a2, max(MAX[tx][a], MAX[tx][b]));
				a = dp[tx][a];
				b = dp[tx][b];
			}
		}
		cout << a1 << " " << a2 << "\n";
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	init();
	solution();
	return 0;
}
