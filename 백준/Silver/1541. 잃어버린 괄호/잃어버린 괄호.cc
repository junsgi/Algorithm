#pragma warning(disable:4996)
#include <stdio.h>
char sic[100];
int result, swi = 1, temp;
int main()
{
	scanf("%s", sic);
	for (int i = 0; sic[i]; i++)
	{
		if (sic[i] == '-' || sic[i] == '+')
		{
			if(sic[i] == '-')
				swi = -1;
			result += temp;
			temp = 0;
		}
		else if('0' <= sic[i] && sic[i] <= '9')
			temp = (10 * temp) + (sic[i] - '0') * swi;

	}
	printf("%d", result + temp);
	return 0;
}
