#pragma warning(disable:4996)
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int n, ex, m, seg[1 << 21], ck[1'000'001];
long long ans;
int query(int left, int right, int idx, int st, int ed)
{
	if (ed < left || right < st) return 0;
	if (st <= left && right <= ed) return seg[idx];
	int mid = (left + right) / 2;
	return query(left, mid, idx * 2, st, ed) + query(mid + 1, right, idx * 2 + 1, st, ed);

}
int insert(int left, int right, int idx, int target)
{
	if (target < left || right < target) return seg[idx];
	if (left == right && target == left) return seg[idx] = 1;
	int mid = (left + right) / 2;
	return seg[idx] = insert(left, mid, idx * 2, target) + insert(mid + 1, right, idx * 2 + 1, target);
}
int main()
{
	cin >> n;
	for (ex = 1; ex < n; ex *= 2);
	for (int i = 0; i < n; i++)
	{
		cin >> m;
		ck[m] = i + 1;
	}

	for (int i = 0; i < n; i++)
	{
		cin >> m;
		ans += query(1, ex, 1, ck[m], ex);
		insert(1, ex, 1, ck[m]);
	}
	cout << ans;
	return 0;
}