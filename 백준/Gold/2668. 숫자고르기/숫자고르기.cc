#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int n, arr[101], visit[101];
vector<int> ans;
void dfs(int node, int st)
{
	if (visit[node])
	{
		if (node == st) ans.push_back(node);
		return;
	}
	visit[node] = 1;
	dfs(arr[node], st);
}
int main()
{
	cin.tie(nullptr); cout.tie(nullptr);
	ios_base::sync_with_stdio(false);
	cin >> n;
	for (int i = 1; i <= n; ++i) cin >> arr[i];
	for (int i = 1; i <= n; ++i)
	{
		fill(visit + 1, visit + n + 1, 0);
		dfs(i, i);
	}
	cout << ans.size() << '\n';
	for (int& i : ans) cout << i << '\n';
	return 0;
}
