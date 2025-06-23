#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
vector<pair<int, int>> map[100001];
int n, m, a, b ,c, s, e, le, ri, mid, ans;
queue<int> que;
bool BFS(int x, int y, int w)
{
	que = queue<int>();
	int freq[100001] = {0,};
	que.push(x);
	freq[x] = 1;
	while (!que.empty())
	{
		int t = que.front();
		que.pop();
		if (t == y) return true;
		for(int i = 0 ; i < (int)map[t].size() ; i++)
		{
			if (freq[map[t][i].first] || map[t][i].second < w) continue;
			freq[map[t][i].first] = 1;
			que.push(map[t][i].first);
		}
	}
	return false;
}
int main()
{
	scanf("%d%d", &n, &m);
	for(int i = 0 ; i < m ; i++)
	{
		scanf("%d%d%d", &a, &b, &c);
		map[a].push_back(make_pair(b, c));
		map[b].push_back(make_pair(a, c));
		ri = max(ri, c);
	}
	scanf("%d%d", &s, &e);
	le = 1;
	while (le <= ri)
	{
		mid = (le + ri) / 2;

		if (BFS(s, e, mid))
		{
			ans = mid;
			le = mid + 1;
		}
		else 
			ri = mid - 1;
	}
	printf("%d", ans);
	return 0;
}
/*
13305
2294 (선택한 동전도
2239
1939
1726
*/