#pragma warning(disable:4996)
#include<stdio.h>
int n, len, arr[100000], st, ed, flag;
char com[100011], ex[311111];
int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%s", com);
		scanf("%d", &len);
		scanf("%s", ex);
		st = 0;
		ed = -1;
		flag = 1;
		if (0 < len)
		{
			int t = 0;
			for (int j = 1; ex[j]; j++)
			{
				if (0 <= (ex[j] - '0') && (ex[j] - '0') <= 9)
					t = t * 10 + (ex[j] - '0');
				else
				{
					arr[++ed] = t;
					t = 0;
				}
			}
		}

		for (int j = 0; com[j]; j++)
		{
			if (com[j] == 'R') flag = -flag;
			else
			{
				if (ed < st)
				{
					printf("error\n");
					flag = 0;
					break;
				}
				if (flag < 0) ed--;
				else st++;
			}
		}
		if (flag == 0) continue;
		else if (flag < 0)
		{
			printf("[");
			for (int j = ed; j >= st; j--)
			{
				if (j != st) printf("%d,", arr[j]);
				else printf("%d", arr[j]);
			}
			printf("]\n");
		}
		else
		{
			printf("[");
			for (int j = st; j <= ed; j++)
			{
				if (j != ed) printf("%d,", arr[j]);
				else printf("%d", arr[j]);
			}
			printf("]\n");
		}
	}
	return 0;
}

