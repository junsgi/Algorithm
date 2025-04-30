#include<iostream>
#include<algorithm>
#include<string>
#include<map>
using namespace std;
int n, m, p[200'000], cnt[200'000];
map<string, int> table;
int find(int node)
{
	if (p[node] == node) return node;
	return p[node] = find(p[node]);
}
int Union(int x, int y)
{
	int fx = find(x), fy = find(y);
	if (fx == fy) return cnt[fx];
	if (fx < fy)
	{
		p[fy] = fx;
		cnt[fx] += cnt[fy];
		cnt[fy] = 0;
		return cnt[fx];
	}
	else
	{
		p[fx] = fy;
		cnt[fy] += cnt[fx];
		cnt[fx] = 0;
		return cnt[fy];
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n;
	for(int i = 0 ; i < n ; i++)
	{
		cin >> m;
		int no = 0, x, y;
		string n1, n2;
		
		// init
		table = map<string, int>();
		for(int j = 0 ; j < 200000 ; j++)
		{
			p[j] = j;
			cnt[j] = 1;
		}

		//solution
		for(int j = 0 ; j < m ; j++)
		{
			cin >> n1 >> n2;
			if (table.find(n1) == table.end())
				table.insert({n1, no++});
			if (table.find(n2) == table.end())
				table.insert({n2, no++});
			x = table[n1]; y = table[n2];
			cout << Union(x, y) << '\n';
		}					
	}
	return 0;
}
