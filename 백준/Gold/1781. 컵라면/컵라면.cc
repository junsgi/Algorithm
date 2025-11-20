#include<iostream>
#define fastio cin.tie(nullptr);cout.tie(nullptr);ios_base::sync_with_stdio(false);
using namespace std;
int n, a, b, len;
pair<int, int> arr[200'000], heap[200'001], tmp[200'000];
void up(int);
void down(int);
void mergeSort(int, int);
int main()
{
	fastio;
	cin >> n;
	for(int i = 0 ; i < n ; ++i)
		cin >> arr[i].first >> arr[i].second;
	mergeSort(0, n - 1);
	for (int i = 0; i < n; ++i)
	{
		heap[++len] = arr[i];
		up(len);
		if (len > arr[i].first)
		{
			heap[1] = heap[len--];
			down(1);
		}
	}
	int ans = 0;
	for (int i = 1; i <= len; ++i) ans += heap[i].second;
	cout << ans;
	return 0;
}
void sort(int st, int ed, int mid)
{
	int a = st, b = mid + 1, t = 0;
	while (a <= mid && b <= ed)
	{
		if (arr[a] < arr[b]) tmp[t++] = arr[a++];
		else tmp[t++] = arr[b++];
	}
	while (a <= mid) tmp[t++] = arr[a++];
	while (b <= ed) tmp[t++] = arr[b++];
	for (int i = 0; i < t; ++i) arr[st + i] = tmp[i];
}
void mergeSort(int st, int ed)
{
	if (st >= ed) return;
	int mid = st + ed >> 1;
	mergeSort(st, mid);
	mergeSort(mid + 1, ed);
	sort(st, ed, mid);
}
int cmp(const pair<int, int>& x, const pair<int, int>& y)
{
	return x.second < y.second;
}
void up(int idx)
{
	if ((idx >> 1) <= 0) return;
	if (cmp(heap[idx], heap[idx >> 1]))
	{
		swap(heap[idx >> 1], heap[idx]);
		up(idx >> 1);
	}
}
void down(int idx)
{
	int child = idx << 1;
	if (child > len) return;
	if ((child | 1) <= len && cmp(heap[child | 1], heap[child]))
		child |= 1;
	if (cmp(heap[child], heap[idx]))
	{
		swap(heap[idx], heap[child]);
		down(child);
	}
}