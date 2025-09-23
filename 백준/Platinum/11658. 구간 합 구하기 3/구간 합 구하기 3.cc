#include <iostream>
#include <vector>
# define fastio cin.tie(nullptr); cout.tie(nullptr); ios_base::sync_with_stdio(false);
using namespace std;
int n, m, k;
vector<vector<int>> seg;
void update(int i, int j, int value)
{
	int x = i - 1 | k, y = j - 1 | k;
	seg[x][y] = value;
	while (y >>= 1)
		seg[x][y] = seg[x][y << 1] + seg[x][y << 1 | 1];
	while (x >>= 1)
	{
		y = j - 1 | k;
		seg[x][y] = seg[x << 1][y] + seg[x << 1 | 1][y];
		while (y >>= 1)
			seg[x][y] = seg[x][y << 1] + seg[x][y << 1 | 1];
	}
}
int yquery(int left, int right, const vector<int>& tmp)
{
	int res = 0;
	--left |= k; --right |= k;
	while (left <= right)
	{
		if (left & 1) res += tmp[left++];
		if (~right & 1) res += tmp[right--];
		left >>= 1;
		right >>= 1;
	}
	return res;
}
int xquery(int left, int right, int yl, int yr)
{
	int res = 0;
	--left |= k; --right |= k;
	while (left <= right)
	{
		if (left & 1) res += yquery(yl, yr, seg[left++]);
		if (~right & 1) res += yquery(yl, yr, seg[right--]);
		left >>= 1;
		right >>= 1;
	}
	return res;
}
int main()
{
	fastio;
	cin >> n >> m;
	for (k = 1; k < n; k <<= 1);
	seg.resize(k << 1);
	for (int i = 1; i < (k << 1); ++i)seg[i].resize(k << 1);
	int w, x1, y1, x2, y2, c;
	for (int i = 1; i <= n; ++i)
	{
		for (int j = 1; j <= n; ++j)
		{
			cin >> c;
			update(i, j, c);
		}
	}
	while (m--)
	{
		cin >> w;
		if (w)
		{
			cin >> x1 >> y1 >> x2 >> y2;
			if (x1 > x2) swap(x1, x2);
			if (y1 > y2) swap(y1, y2);
			cout << xquery(x1, x2, y1, y2) << '\n';
		}
		else
		{
			cin >> x1 >> y1 >> c;
			update(x1, y1, c);
		}
	}
	return 0;
}