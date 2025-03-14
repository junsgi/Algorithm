#include<stdio.h>
int main()
{
	int n, cnt = 0, temp = 0, sum = 0;
	scanf("%d", &n);
	if (n <= 10) printf("%d", n);
	else
	{
		cnt = 10;
		for(int i = 11; i <= n ; i++)
		{
			temp = i; sum = 0;
			while(temp != 0 )
			{
				sum += temp % 10;
				temp /= 10;
			}
			if (i % sum == 0) cnt++;
		
		}
		printf("%d", cnt);
	}

	return 0;
}