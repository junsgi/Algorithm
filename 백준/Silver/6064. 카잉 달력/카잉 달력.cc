#pragma warning(disable:4996)
#include<stdio.h>
int t, m, n, x, y;
int gcd(int i, int j)
{
    int c = 0;
    while (j)
    {
        c = i;
        i = j;
        j = c % j;
    }
    return i;
}
int main()
{
    scanf("%d", &t);
    while (t--)
    {
        scanf("%d%d%d%d", &m, &n, &x, &y); 
        int ans = x;
        while (ans <= m * n / gcd(m, n))
        {
            if ((ans - 1) % n + 1 == y)
                break;
            ans += m;
        }
        if (ans > m * n / gcd(m, n))
            printf("-1\n");
        else
            printf("%d\n", ans);
    }
    return 0;
}