#include<stdio.h>
int a, b, c;
int main()
{
    scanf("%d%d%d", &a, &b, &c);
    int res = a;
    if (b >= 1000) res = res * 10000 + b;
    else if (b >= 100) res = res * 1000 + b;
    else if (b >= 10) res = res * 100 + b;
    else res = res * 10 + b;
    printf("%d\n%d", a + b - c, res - c);
    return 0;
}