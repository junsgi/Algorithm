#pragma warning(disable:4996)
#include<stdio.h>
#include<vector>
#include<queue>
using namespace std;
struct Node {
	int n, bit;
	Node(int _n, int _bit) : n(_n), bit(_bit) {}
};
struct Temp { int n, w; };
int n, m, k, treasure[101], visit[1 << 14][101], answer;
vector<Temp> graph[101];
queue<Node> que;
int func(int n) 
{
	int cnt = 0;
	while (n)
	{
		cnt += n % 2;
		n /= 2;
	}
	return cnt;
}
int main()
{
	scanf("%d%d%d", &n, &m, &k);
	for (int i = 1; i <= n; i++) treasure[i] = -1;
	for (int i = 0; i < k; i++)
	{
		int tmp;
		scanf("%d", &tmp);
		treasure[tmp] = i;
	}
	for (int i = 0; i < m; i++)
	{
		int a, b, c;
		scanf("%d%d%d", &a, &b, &c);
		graph[a].push_back({ b, c });
		graph[b].push_back({ a, c });
	}
	que.emplace(1, 0);
	visit[0][1] = 1;
	while (!que.empty())
	{
		Node element = que.front(); que.pop();
		int node = element.n, bit = element.bit, cnt = func(bit);
		if (node == 1 && cnt > 0) {
			answer = answer < cnt ? cnt : answer;
			continue;
		}
		for (Temp& i : graph[node])
		{
			if (cnt > i.w) continue;
			if (treasure[i.n] >= 0 && !visit[bit | (1 << treasure[i.n])][i.n]) // 줍는다.
			{
				que.emplace(i.n, bit | (1 << treasure[i.n]));
				visit[bit | (1 << treasure[i.n])][i.n] = 1;
			}
			if (!visit[bit][i.n]) // 안 줍는다.
			{
				que.emplace(i.n, bit);
				visit[bit][i.n] = 1;
			}
		}
	}
	printf("%d", answer);
	return 0;
}
