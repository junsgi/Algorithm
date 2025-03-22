#include<stdio.h>
int main()
{
    int a, b, c;
    scanf("%d%d%d", &a, &b, &c);
    int n = (c - a) / (a - b);
    if ((c - a) % (a - b) != 0) n++;
    printf("%d", n + 1);
    return 0;
}
