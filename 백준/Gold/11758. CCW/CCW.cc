#include <stdio.h>
int main()
{
    int a, b, c, d, e, f;
    scanf("%d%d%d%d%d%d", &a, &b, &c, &d, &e, &f);
    int res = (a * d + c * f + e * b) - (c * b + e * d + a * f);
    if (res < 0) printf("-1");
    else if (res > 0) printf("1");
    else printf("0");
    return 0;
}