#pragma warning(disable:4996)
#include<stdio.h>
#define M 1000
int n, matrix[5][5], tmp[5][5], ans[5][5];
long long b;
void mul(int(&x)[5][5], int(&y)[5][5])
{
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
        {
            tmp[i][j] = 0;
            for (int k = 0; k < n; k++)
                tmp[i][j] = (tmp[i][j] + (x[i][k] * y[k][j] % M)) % M;
        }
    for (int i = 0; i < n * n; i++) x[i / n][i % n] = tmp[i / n][i % n];
}
int main()
{
    scanf("%d%lld", &n, &b);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            scanf("%d", &matrix[i][j]);
        ans[i][i] = 1;
    }
    while (b > 0)
    {
        if (b & 1) mul(ans, matrix);
        mul(matrix, matrix);
        b /= 2;
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            printf("%d ", ans[i][j]);
        printf("\n");
    }
    return 0;
}
