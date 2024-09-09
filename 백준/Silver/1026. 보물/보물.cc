#pragma warning(disable:4996)
#include <stdio.h>
#include<algorithm>
using namespace std;
int n, ans;
int a[110], b[110];
int rev(int x, int y)
{
	return x > y;
}
int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++) scanf("%d", &a[i]);
	for (int i = 0; i < n; i++) scanf("%d", &b[i]);
	sort(a, a + n);
	sort(b, b + n, rev);
	for (int i = 0; i < n; i++)
		ans += a[i] * b[i];
	printf("%d", ans);
	return 0;
}