#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
using namespace std;
long long a, b, c, d, e, f, g, h;
int ccw(long long i, long long j,
        long long k, long long x,
        long long y, long long z)
{
    long long res = (i * x + k * z + y * j) - (k * j + y * x + i * z);
    if (res < 0) return -1;
    else if (res > 0) return 1;
    return 0;
}
int main()
{
    scanf("%lld%lld%lld%lld%lld%lld%lld%lld", &a, &b, &c, &d, &e, &f, &g, &h);
    int case1 = ccw(a, b, c, d, e, f) * ccw(a, b, c, d, g, h);
    int case2 = ccw(e, f, g, h, a, b) * ccw(e, f, g, h, c, d);
    int res = 0;
    // (a, b), (c, d), (e, f), (g, h)
    if (case1 == 0 && case2 == 0)
        res = min(a, c) <= max(e, g) && min(e, g) <= max(a, c) && min(b, d) <= max(f, h) && min(f, h) <= max(b, d);
    else if (case1 <= 0 && case2 <= 0)
        res = 1;
    printf("%d", res);
    return 0;
}
