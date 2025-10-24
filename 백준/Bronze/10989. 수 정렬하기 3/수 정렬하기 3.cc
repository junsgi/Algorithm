#pragma warning(disable:4996)
#include <stdio.h>
#include <algorithm>
using namespace std;
int n, s, sw, ans;
int freq[10000];
int le, ri, mid;
int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &le);
		if (ri < le) ri = le;
		freq[le]++;
	}
	for (int i = 1; i <= ri; i++)
	{
		if (freq[i])
		{
			while (freq[i])
			{
				printf("%d\n", i);
				freq[i]--;
			}
		}
	}
	return 0;
}