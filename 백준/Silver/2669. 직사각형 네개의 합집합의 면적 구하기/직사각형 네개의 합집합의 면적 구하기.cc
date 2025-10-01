#include <iostream>
using namespace std;
int org_x[8], org_y[8], x[8], y[8], tmp[8];
void mergeSort(int st, int ed, int(&arr)[8])
{
	int idx = 0;
	int mid = st + ed >> 1;
	int left = st, right = mid + 1;
	while (left <= mid && right <= ed)
	{
		if (arr[left] < arr[right]) tmp[idx++] = arr[left++];
		else tmp[idx++] = arr[right++];
	}
	while (left <= mid) tmp[idx++] = arr[left++];
	while (right <= ed) tmp[idx++] = arr[right++];
	for (int i = 0; i < idx; ++i) arr[st + i] = tmp[i];
}
void merge(int st, int ed, int (&arr)[8])
{
	if (st >= ed) return;
	int mid = st + ed >> 1;
	merge(st, mid, arr);
	merge(mid + 1, ed, arr);
	mergeSort(st, ed, arr);
}
int check(int x1, int y1, int x2, int y2)
{
	int hit = 0;
	for (int i = 1; !hit && i < 8; i += 2)
	{
		if (org_x[i - 1] <= x1 && x2 <= org_x[i] && org_y[i - 1] <= y1 && y2 <= org_y[i])
			hit = 1;
	}
	return hit;
}
int main()
{
	for (int i = 1; i < 8; i += 2)
	{
		cin >> org_x[i - 1] >> org_y[i - 1] >> org_x[i] >> org_y[i];
		x[i - 1] = org_x[i - 1]; y[i - 1] = org_y[i - 1];
		x[i] = org_x[i]; y[i] = org_y[i];
	}
	merge(0, 7, x); merge(0, 7, y);
	int ans = 0;
	for (int i = 1; i < 8; ++i)
	{
		if (x[i] == x[i - 1]) continue;
		int x1 = x[i - 1], x2 = x[i];
		for (int j = 1; j < 8; ++j)
		{
			if (y[j - 1] == y[j]) continue;
			int y1 = y[j - 1], y2 = y[j];
			if (check(x1, y1, x2, y2))
				ans += (y2 - y1) * (x2 - x1);
		}
	}
	cout << ans;
	return 0;
}
