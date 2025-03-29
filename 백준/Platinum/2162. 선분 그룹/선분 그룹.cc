// CCW + Union Find
#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
using namespace std;
struct Temp { int x1, y1, x2, y2; };
int n, p[3000], cnt[3000], ans, c;
Temp arr[3000];
int find(int x) 
{
	if (p[x] == x) return x;
	return p[x] = find(p[x]);
}
void Union(int x, int y)
{
	int fx = find(x), fy = find(y);
	if (fx == fy) return;
	if (fx < fy)
	{
		p[fy] = fx;
		cnt[fx] += cnt[fy];
		cnt[fy] = 0;
	}
	else
	{
		p[fx] = fy;
		cnt[fy] += cnt[fx];
		cnt[fx] = 0;
	}
}
int CCW(int a, int b, int c, int d,	int e, int f)
{
	int res = (a * d + c * f + e * b) - (c * b + e * d + a * f);
	if (res < 0) return -1;
	else if (res > 0) return 1;
	return 0;
}
bool cmp(Temp& a, Temp& b)
{
	return min(a.x1, a.x2) <= max(b.x1, b.x2) && min(b.x1, b.x2) <= max(a.x1, a.x2) && min(a.y1, a.y2) <= max(b.y1, b.y2) && min(b.y1, b.y2) <= max(a.y1, a.y2);
}
int func(int i, int j)
{
	int i1 = CCW(arr[i].x1, arr[i].y1, arr[i].x2, arr[i].y2, arr[j].x1, arr[j].y1);
	int i2 = CCW(arr[i].x1, arr[i].y1, arr[i].x2, arr[i].y2, arr[j].x2, arr[j].y2);
	int j1 = CCW(arr[j].x1, arr[j].y1, arr[j].x2, arr[j].y2, arr[i].x1, arr[i].y1);
	int j2 = CCW(arr[j].x1, arr[j].y1, arr[j].x2, arr[j].y2, arr[i].x2, arr[i].y2);

	if (i1 * i2 == 0 && j1 * j2 == 0)
		return cmp(arr[i], arr[j]);
	else if (i1 * i2 <= 0 && j1 * j2 <= 0)
		return 1;
	return 0;
}
int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d%d%d%d", &arr[i].x1, &arr[i].y1, &arr[i].x2, &arr[i].y2);
		p[i] = i;
		cnt[i] = 1;
	}
	for (int i = 0; i < n - 1; i++)
		for (int j = i + 1; j < n; j++)
			if (func(i, j))
				Union(i, j);

	for (int i = 0; i < n; i++)
	{
		if (p[i] == i)
			ans++;
		c = c < cnt[i] ? cnt[i] : c;
	}
	printf("%d\n%d", ans, c);
	return 0;
}
