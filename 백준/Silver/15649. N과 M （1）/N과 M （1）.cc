#include<stdio.h>
int dab[10], n, m;
int c[11];
void pro(int k)
{
	if (k == m)
	{
		for(int i = 0 ; i < m ; i++)
			printf("%d ", dab[i]);
		printf("\n");
		return;
	}

	for(int d = 1 ; d <= n ; d++)
	{
		if (c[d]) continue;
		dab[k] = d;

		c[d] = 1;
		pro(k + 1);
		c[d] = 0;
	}
}
int main()
{
	scanf("%d%d", &n, &m);
	pro(0);
	return 0;
}