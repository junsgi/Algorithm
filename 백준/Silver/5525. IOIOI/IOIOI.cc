#pragma warning(disable:4996)
#include<stdio.h>
int n, m, st, ed, cnt, ans[1000001];
char io[1000011];
int main()
{
	scanf("%d%d", &n, &m);
	scanf("%s", io);
	while (st <= ed && st < m)
	{
		if (io[st] == 'O')
		{
			st++; ed++;
			continue;
		}
		ed += 2;
		if (ed < m && io[ed - 1] == 'O' && io[ed] == 'I')
			cnt++;
		else
		{
			st = ed = ed - 1;
			if (cnt > 0)
				for (int i = 1; i <= cnt; i++)
					ans[i] += cnt - i + 1;
			cnt = 0;
		}
	}
	printf("%d", ans[n]);
	return 0;
}

