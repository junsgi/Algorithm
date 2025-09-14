#include<stdio.h>
int main()
{
    int n, m, i, j, k;
    int arr[101] = {0, };
    scanf("%d%d", &n, &m);
    while(m--)
    {
        scanf("%d%d%d", &i, &j, &k);
        for(int __ = i ; __ <= j ; ++__)
            arr[__] = k;
    }
    for(int a = 1 ; a <= n ; ++a)
        printf("%d ", arr[a]);
    return 0;
}