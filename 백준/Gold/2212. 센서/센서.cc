#pragma warning(disable:4996)
#include <stdio.h>
#include<algorithm>
using namespace std;
int n, k, ans;
int arr[10100];
int temp[10010];
int check(int x, int y)
{
	return x > y;
}
int main()
{
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);
	sort(arr, arr + n);
	ans = arr[n - 1] - arr[0];
	for (int i = 1; i < n; i++)
		temp[i - 1] = arr[i] - arr[i - 1];
	sort(temp, temp + n - 1, check);
	for (int i = 0; i < k - 1; i++)
		ans -= temp[i];
	printf("%d", ans);
	return 0;
}