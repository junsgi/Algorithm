#include<stdio.h>
int n, m, p[200], a;
int find(int x)
{
	if (p[x] == x) return x;
	return p[x] = find(p[x]);
}
void Union(int x, int y)
{
	int fx = find(x), fy = find(y);
	if (fx < fy)
		p[fy] = fx;
	else if (fx > fy)
		p[fx] = fy;
}
int main()
{
	scanf("%d%d", &n, &m);
    for(int i = 0 ; i < n ; i++) p[i] = i;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			scanf("%d", &a);
			if (a) Union(i, j);
		}
	}
	int start;
	scanf("%d", &start);
	start = find(start - 1);
	for (int i = 0; i < m - 1; i++)
	{
		scanf("%d", &a);
		if (start != find(a - 1))
		{
			printf("NO");
			return 0;
		}
	}
	printf("YES");
	return 0;
}