#pragma warning(disable:4996)
#include<iostream>
#include<algorithm>
#define M 5'000'000'000ll
using namespace std;
typedef long long ll;
ll n, ex, m;
pair<int, ll> seg[(1 << 18) + 1];

pair<int, ll> query(ll left, ll right, ll idx, ll st, ll ed)
{
	if (right < st || ed < left) return { 0, M };
	if (st <= left && right <= ed) return seg[idx];
	ll mid = (left + right) / 2;
	pair<int, ll> l = query(left, mid, idx * 2, st, ed);
	pair<int, ll> r = query(mid + 1, right, idx * 2 + 1, st, ed);
	if (l.second < r.second) return l;
	else return r;
}

pair<int, ll> insert(ll left, ll right, ll idx, int target)
{
	if (target < left || right < target) return seg[idx];
	if (left == right && left == target) return seg[idx] = { target, m };
	ll mid = (left + right) / 2;
	pair<int, ll> l = insert(left, mid, idx * 2, target);
	pair<int, ll> r = insert(mid + 1, right, idx * 2 + 1, target);
	if (l.second < r.second) seg[idx] = l;
	else seg[idx] = r;
	return seg[idx];
}

ll pro(ll left, ll right)
{
	if (left > right) return 0;
	pair<int, ll> value = query(1, ex, 1, left, right);
	if (left == right) return value.second;
	return max(value.second * (right - left + 1), max(pro(left, value.first - 1), pro(value.first + 1, right)));
}
int main()
{
	while (1)
	{
		cin >> n;
		if (!n) break;
		for (ex = 1; ex < n; ex *= 2);
		for (int i = 1; i < ex * 2 + 1; i++) { seg[i].first = 0; seg[i].second = M; }
		for (int i = 0; i < n; i++)
		{
			cin >> m;
			insert(1, ex, 1, i + 1);
		}
		cout << pro(1, n) << '\n';

	}
	return 0;
}