#include<iostream>
#include<algorithm>
#define fastio ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
using namespace std;
int n, m, arr[200'000];
int get_next(int st, int target)
{
	int left = st - 1, right = n;
	while (left + 1 < right)
	{
		int mid = (left + right) >> 1;
		if (arr[mid] < target) left = mid;
		else right = mid;
	}
	return right;
}
int main() 
{
	fastio;
	cin >> n >> m;
	for (int i = 0; i < n; ++i) cin >> arr[i];
	sort(arr, arr + n);
	int left = -1, right = 1'000'000'001;
	while (left + 1 < right)
	{
		int mid = left + right >> 1;
		int idx = 0;
		for (int i = 1; idx < n && i < m; ++i)
			idx = get_next(idx + 1, arr[idx] + mid);
		if (idx < n) left = mid;
		else right = mid;
	}
	cout << left;
	return 0;
}