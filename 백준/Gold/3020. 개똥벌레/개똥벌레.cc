#pragma warning(disable:4996)
#include<stdio.h>
long long n, m, arr[500'002], ans = 0x7fffffff, cnt;
int main()
{
    scanf("%lld%lld", &n, &m);
    for (int i = 0; i < n; i++)
    {
        int a;
        scanf("%d", &a);
        if ((i & 1) == 0)
        {
            arr[1]++;
            arr[a + 1]--;
        }
        else
        {
            arr[m - a + 1]++;
            arr[m + 1]--;
        }
    }
    for (int i = 1; i <= m ;i++)
    {
        arr[i] += arr[i - 1];
        if (arr[i] < ans)
        {
            cnt = 1;
            ans = arr[i];
        }
        else if (arr[i] == ans)cnt++;
    }

    printf("%lld %lld", ans, cnt);
    return 0;
}