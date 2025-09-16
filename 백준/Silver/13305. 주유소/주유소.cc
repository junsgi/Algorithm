#include <stdio.h>
#include <algorithm>
using namespace std;
int n;
long long a, d[100010], cost[100010], m = 0x7fffffff;
int main()
{
	scanf("%d", &n);
	for(int i = 0 ; i < n - 1; i++)
		scanf("%lld", &d[i]);
	for(int i = 0 ; i < n ; i++)
		scanf("%lld", &cost[i]);

	for(int i = 0; i < n - 1 ; i++)
	{
		m = min(m, cost[i]);
		a += d[i] * m;
	}
	printf("%lld", a);
	return 0;
}
