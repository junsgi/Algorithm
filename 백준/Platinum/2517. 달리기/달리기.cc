#include<stdio.h>
#include<algorithm>
using namespace std;
struct Temp
{
	int n, idx;
}arr[500000];
int n, m, seg[1<<20];
int cmp(Temp a, Temp b) { return a.n > b.n; }
int cmp2(Temp a, Temp b) { return a.idx < b.idx; }
int insert(int left, int right, int idx, int target)
{
	if (left == target && right == target)
		return seg[idx] = 1;
	if (left == right || target < left || right < target) return seg[idx];
	int mid = (left + right) / 2;
	return seg[idx] = insert(left, mid, idx * 2, target) + insert(mid + 1, right, idx * 2 + 1, target);
}
int query(int left, int right, int idx, int st, int ed)
{
	if (ed < left || right < st) return 0;
	if (st <= left && right <= ed) return seg[idx];
	int mid = (left + right) / 2;
	return query(left, mid, idx * 2, st, ed) + query(mid + 1, right, idx * 2 + 1, st, ed);
}
int main()
{
	scanf("%d", &n);
	int cnt = 1;
	for (; cnt < n; cnt *= 2);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &arr[i].n);
		arr[i].idx = i;
	}
	sort(arr, arr + n, cmp);
	for (int i = 0; i < n; i++)
		arr[i].n = i + 1;
	sort(arr, arr + n, cmp2);
	for (int i = 0; i < n; i++)
	{
		printf("%d\n", 1 + query(1, cnt, 1, 1, arr[i].n - 1));
		insert(1, cnt, 1, arr[i].n);
	}
		
	return 0;
}
