#include<stdio.h>
#include<algorithm>
using namespace std;
int n, ans, t1, t2;
struct temp{
	int a, b;
}ar[10010];
int check(temp x, temp y)
{
	return x.b < y.b || x.b == y.b && x.a < y.a;
}
int main()
{
	scanf("%d", &n);
	for(int i = 0 ; i < n ; i++)
		scanf("%d%d", &ar[i].a, &ar[i].b);
	sort(ar, ar+n, check);

	ans = ar[1].a - ar[0].a;
	ans += ar[n - 1].a - ar[n - 2].a;
	
	for(int i = 1 ; i < n - 1; i++)
	{
		t1 = t2 = 0;
		if (ar[i].b == ar[i-1].b)
			t1 = ar[i].a - ar[i-1].a;
		if (ar[i].b == ar[i + 1].b)
			t2 = ar[i+1].a - ar[i].a;

		if (t1 == 0)
			ans += t2;
		else if (t2 == 0)
			ans += t1;
		else ans += min(t1, t2);
	}
	printf("%d", ans);
	return 0;
}
