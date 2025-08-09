#pragma warning(disable:4996)
#include <stdio.h>
#include<algorithm>
#include<vector>
using namespace std;
int x, y, n, ay, t1, t2, cnt, idx, ans;
int a[401];
int main()
{
	scanf("%d%d%d", &x, &y, &n);
	for (int i = 1; i <= n + 1; i++)
	{
		scanf("%d%d", &t1, &t2);
		if (t1 == 1) a[t2] = i;
		else if (t1 == 2) a[x * 2 + y - t2] = i;
		else if (t1 == 3) a[x * 2 + y * 2 - t2] = i;
		else a[x + t2] = i;

		if (i == n + 1)
		{
			if (t1 == 1) ay = t2;
			else if (t1 == 2) ay = x * 2 + y - t2;
			else if (t1 == 3) ay = x * 2 + y * 2 - t2;
			else ay = x + t2;
		}
	}
	for (int i = 1; i <= n; i++)
	{
		t1 = cnt = 0;
		idx = ay; 
		while (1)
		{
			cnt++;
			idx++;
			if (idx > x * 2 + y * 2) idx = 1;
			if (a[idx] == i) { t1 = cnt; break; }
		}
		t2 = cnt = 0;
		idx = ay;
		while (1)
		{
			cnt++;
			idx--;
			if (idx < 1) idx = x * 2 + y * 2;
			if (a[idx] == i) { t2 = cnt; break; }
		}
		ans += min(t1, t2);
	}
	printf("%d", ans);
	return 0;
}
/*
1 -> second or 
4 -> x + second or 
2 -> x * 2 + y - second or 
3 -> x * 2 + y * 2 - second
*/